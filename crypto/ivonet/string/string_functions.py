#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from ivonet.collection.dictinary import sort_by_value_then_key
from ivonet.woorden.woordenboek import Woordenboek


def sort_alphabetical(txt, reverse=False) -> str:
    return "".join(sorted(txt, reverse=reverse))


def is_sorted(txt, reverse=False) -> bool:
    return txt == sort_alphabetical(txt, reverse=reverse)


def letters(txt, index=0):
    """return the indexed letter of words"""
    words = txt.split(" ")
    return ''.join([x[index] for x in words])


def letters_is_word(txt, index=0):
    wb = Woordenboek()
    return wb.is_word(letters(txt, index))


class FrequencyDict(object):

    def __init__(self, lst=None) -> None:
        self.dictionary = {}
        if lst:
            self.put_all(lst)

    def put_all(self, name: list) -> None:
        [self.put(x) for x in name]

    def put(self, name: str) -> None:
        if name in self.dictionary.keys():
            self.dictionary[name] = self.dictionary[name] + 1
        else:
            self.dictionary[name] = 1

    def list(self, reverse=False) -> list:
        return sort_by_value_then_key(self.dictionary, reverse=reverse)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        template = "{:>20} => {:>1}"
        return "\n".join([template.format(word, value) for word, value in self.list()])

    def frequency(self, word) -> int:
        return self.dictionary[word]

    def pop(self, reverse=False) -> tuple:
        ret = sort_by_value_then_key(self.dictionary, reverse=reverse)
        if not ret:
            return None, None
        ret = ret[0]
        del (self.dictionary[ret[0]])
        return ret


def word_frequency_counter(lst):
    return FrequencyDict(lst)


def initialize(payload) -> str:
    """Returns the first letters of every word in the payload as a single string"""
    let = []
    for word in payload.upper().split():
        let.append(word[0])
    return "".join(let)
