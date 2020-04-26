#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import re

from ivonet.collection.dictinary import sort_by_value_then_key
from ivonet.collection.list import list_equal
from ivonet.file import un_pickle, in_pickle, txt_file_upper_lines
from ivonet.log import _

# https://www.mtholyoke.edu/courses/quenell/s2003/ma139/js/count.html
# See for some of the functionality the unittests of this package

_DEBUG = False

PAT_NON_ALPHANUMERIC = re.compile("[\W_]+", re.UNICODE)


def met_lengte(number):
    return txt_file_upper_lines("%s_letters_no_diacritics.txt" % number)


def open_taal_woorden_1():
    return txt_file_upper_lines("basiswoorden_OpenTaal_200G_no_diacritics.txt")


def open_taal_woorden_2():
    return txt_file_upper_lines("OpenTaal-210G-basis-gekeurd_no_diacritics.txt")


def open_taal_woorden_flexie():
    return txt_file_upper_lines("OpenTaal-210G-flexievormen_no_diacritics.txt")


def mijn_woorden():
    return txt_file_upper_lines("woorden.txt")


def wilhelmus_orig():
    return txt_file_upper_lines("wilhelmus_no_diacritics_words.txt")


def wilhelmus_modern():
    return txt_file_upper_lines("wilhelmus_modern_no_diacritics_words.txt")


def dutch():
    return txt_file_upper_lines("dutch_no_diacritics.txt")


def all_words():
    woorden_ = {'2': met_lengte(2), '3': met_lengte(3), '4': met_lengte(4), '5': met_lengte(5), '6': met_lengte(6),
                '7': met_lengte(7), '8': met_lengte(8), '9': met_lengte(9),
                'OpenTaal_1': open_taal_woorden_1(),
                'OpenTaal_2': open_taal_woorden_2(),
                'OpenTaal_flexie': open_taal_woorden_flexie(),
                'mijn_woorden': mijn_woorden(),
                'dutch': dutch(),
                'wilhelmus_orig': wilhelmus_orig(),
                'wilhelmus_modern': wilhelmus_modern(),
                'straat_taal': txt_file_upper_lines("straat_taal_woorden.txt"),
                }
    _(woorden_)
    return woorden_


def char_frequency(value, remove_whitespace=True, ignore_case=True) -> dict:
    """Calculates the char frequency of a word and returns a dict"""
    frequency_matrix = {}
    wurth = value
    if ignore_case:
        wurth = wurth.upper()
    if remove_whitespace:
        wurth = PAT_NON_ALPHANUMERIC.sub("", wurth)
    for n in wurth:
        keys = frequency_matrix.keys()
        if n in keys:
            frequency_matrix[n] += 1
        else:
            frequency_matrix[n] = 1
    _("created char_frequency for word {} : {}".format(value, frequency_matrix))
    return frequency_matrix


def calculate_distance(word) -> list:
    """Calculates how many of each letter is needed to match the letter frequented most in the string"""
    freq = char_frequency(word)
    freq = sort_by_value_then_key(freq)
    letter, tot = freq.pop()
    return [(l, tot - n) for l, n in freq]


class Word(object):
    """Represents a word.
    Not sure if Ill use it?!
    """

    def __init__(self, word) -> None:
        self.word = word
        self.signature = None
        self.__create_signature__()

    def get_signature(self) -> str:
        return self.signature

    def __create_signature__(self):
        freq = char_frequency(self.word)
        self.signature = sort_by_value_then_key(freq, reverse=True)


class Woordenboek(object):
    def __init__(self) -> None:
        self.signatures_file = "signatures_db.pickle"
        self.woorden_file = "woorden_db.pickle"
        self.signatures = {}
        self.woorden = {}
        self.load_db()

    def load_db(self) -> None:
        """Loads the pickle database or triggers a rebuild if none exist.

        Note:
        Just delete all pickle files and they will be recreated first time called.
        """
        self.signatures = un_pickle(self.signatures_file)
        if not self.signatures:
            self.build_db()
        self.woorden = un_pickle(self.woorden_file)
        if not self.woorden:
            self.build_db()

    def build_db(self) -> None:
        """Rebuilds the pickle database"""
        _("Build DB started")
        all = all_words()
        _(all)
        for key in all.keys():
            for wrd in all[key]:
                self.word_signature(wrd)
        self.save_state()

    def equal_number_of_letters(self, value) -> bool:
        """Checks if a certain dictionary has all chars in equal measure"""
        return list_equal(list(value.values()))

    def multiples_with_length(self, lengte) -> dict:
        """Finds all multiples based on a length
        I guess this function really has no reason to exist anymore because all doubles will be
        found when the database is created, but it might be usefull again in the future
        """
        pickle_file = "{}_multiples.pickle".format(lengte)
        un_pickled = un_pickle(pickle_file)
        if un_pickled:
            return un_pickled
        answer = {}
        for wrd in met_lengte(lengte):
            signature = self.word_signature(wrd)
            ret = self.by_signature(signature)
            if len(ret) > 1:
                answer[signature] = ret
        in_pickle(pickle_file, answer)
        return answer

    def __by_signature(self, signature) -> list:
        """The actual calculation of a signature if it can not be retrieved"""
        length = 0
        for x in list(signature):
            if x.isdigit():
                length += int(x)
        woorden = met_lengte(length)
        found = []
        [found.append(x) for x in woorden if self.word_signature(x) == signature]
        return found

    def by_signature(self, signature) -> list:
        """Finds all words belonging to a signature"""
        woorden = None
        if self.signatures:
            woorden = self.signatures.get(signature)
        if not woorden:
            woorden = self.__by_signature(signature)
            self.signatures[signature] = list(set(woorden))
        return woorden

    def by_word(self, word):
        """find all equal words based on the signature of the provided word."""
        return self.by_signature(self.word_signature(word.upper()))

    def by_len(self, length):
        """find all words of a length"""
        return [x for x in self.woorden.keys() if len(x) == length]

    def by_len_and_containing_letters(self, length, containing, not_containing=None):
        """find all words of a length and containing all the letters provided.
        So there should be equal or less letters given then the length.
        if not_containing is provided it will also check that none of those letters are in the word
        """
        if length < len(containing):
            _("The number of letters that have to exists are more then the length asked for.")
            return []

        def has_letters(word, letters):
            ret = word
            for letter in letters:
                if letter not in ret:
                    return False
                else:
                    ret = ret.replace(letter, "", 1)
            return True

        def not_has_letters(word, letters):
            for letter in word:
                if letter in letters:
                    return False
            return True

        if not_containing:
            return [x for x in self.by_len(length)
                    if has_letters(x, containing.upper())
                    and not_has_letters(x, not_containing.upper())]
        return [x for x in self.by_len(length) if has_letters(x, containing.upper())]

    def by_same_word_plus_one_letter(self, value):
        """
        Find words containing the word given, in same letter ordering, but with one letter more added to it somewhere
        """
        word = value.upper()
        words = self.by_len_and_containing_letters(len(word) + 1, word)
        ret = []
        for wrd in words:
            for i, letter in enumerate(list(wrd)):
                new = wrd[:i] + wrd[(i + 1):]
                if word == new:
                    ret.append(wrd)
                    break
        return ret

    def by_letters(self, letters) -> list:
        """
        Find all words containing letters provided
        """
        answer = []
        for word in self.woorden.keys():
            found = True
            for letter in word:
                if not letter in letters:
                    found = False
                    break
            if found:
                answer.append(word)
        return answer

    def anagram(self, word) -> list:
        """
        Returns all anagrams of a provided word.
        """
        return self.by_word(word.upper())

    def is_word(self, word):
        return word.upper() in self.woorden.keys()

    def find_all_in_signature(self, inputList) -> dict:
        """"""
        if not inputList:
            return {}
        signatures = self.signatures
        for item in inputList:
            signatures = [s for s in signatures if item in s]
        answer = {}
        for sig in signatures:
            answer[sig] = self.signatures.get(sig)
        return answer

    def find_all_fitting(self, sentence):
        """HERE AM I"""
        dist = calculate_distance(sentence)
        answer = {}
        cur_num = 0
        first = True
        for l, n in dist[::-1]:
            answer.update(self.find_all_in_signature((l, n)))
        print(answer)

    def __word_signature(self, word):
        freq = char_frequency(word)
        freq = sort_by_value_then_key(freq, reverse=True)
        sig = ["{}{}".format(a, b) for a, b in freq]
        sig = "".join(sig)
        self.add(word, sig)
        return sig

    def word_signature(self, word):
        """Provides the signature of a word"""
        signature = self.woorden.get(word.upper(), None)
        if not signature:
            signature = self.__word_signature(word)
        return signature

    def ends_with_signature(self, value):
        signature = sort_by_value_then_key(char_frequency(value), reverse=True)
        input_list = ["{}{}".format(l, n) for l, n in signature]
        in_signature = self.find_all_in_signature(input_list)
        answer = []
        for items in in_signature.values():
            for item in items:
                if str(item).endswith(value.upper()):
                    answer.append(item)
        return answer

    def ends_with(self, value) -> list:
        end = value.upper()
        return [x for x in self.woorden if x.endswith(end)]

    def ends_with_by_len(self, value, size) -> list:
        """
        Get a list of words ending with the value and having a length of 'size'

        :param value: the letter(s) it should end with
        :param size: the size/len of the word
        :return: list of words
        """
        return [x for x in self.ends_with(value) if len(x) == size]

    def starts_with(self, value) -> list:
        start = value.upper()
        return [x for x in self.woorden if x.startswith(start)]

    def contains(self, value) -> list:
        has = value.upper()
        return [x for x in self.woorden if has in x]

    def not_contains(self, letters) -> list:
        """Returns all words not containing the string of letters provided"""
        answer = list(self.woorden.keys())
        for word in self.woorden.keys():
            for letter in list(letters):
                if letter in word:
                    answer.remove(word)
                    break
        return answer

    def not_contains_with_length(self, letters, length):
        woorden = self.by_len(length)
        answer = woorden[:]
        for word in woorden:
            for letter in list(letters):
                if letter in word:
                    answer.remove(word)
                    break
        return answer

    def add(self, word, signature):
        """Add a word to the dictionary and the singature too"""
        self.woorden[word] = signature
        existing_woord_lijst = self.signatures.get(signature, [])
        existing_woord_lijst.append(word)
        self.signatures[signature] = list(set(existing_woord_lijst))

    def save_state(self):
        """saves the sate of the class for performance gain.
        Will be loaded at instantiation of the class
        """
        in_pickle(self.woorden_file, self.woorden)
        in_pickle(self.signatures_file, self.signatures)

    def __str__(self) -> str:
        return str(self.signatures)


def rebuild():
    """run me if you want to rebuild the database pickle files"""
    wb = Woordenboek()
    wb.build_db()  # if you want to reindex the pickles! or throw the pickles away... they will be recreated when needed


def cli():
    wb = Woordenboek()
    run = True
    while run:
        run = input("is_word check: ")
        if run:
            print(wb.is_word(run), wb.word_signature(run), wb.anagram(run))


def woorden_by_size(size):
    wb = Woordenboek()
    print(wb.by_len(size))


if __name__ == '__main__':
    # woorden_by_size(40)
    rebuild()
    cli()
