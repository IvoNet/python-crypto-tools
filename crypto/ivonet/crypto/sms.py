#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import itertools

from ivonet.collection.dictinary import invert_dict
from ivonet.woorden.woordenboek import Woordenboek


class Sms(object):
    """SMS class for translating words to sms numbers or vise versa"""

    def __init__(self) -> None:
        self.SMS_KEYBOARD = {"A": 2, "B": 2, "C": 2, "D": 3, "E": 3, "F": 3, "G": 4, "H": 4, "I": 4, "J": 5, "K": 5,
                             "L": 5, "M": 6,
                             "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7, "S": 7, "T": 8, "U": 8, "V": 8, "W": 9, "X": 9,
                             "Y": 9, "Z": 9,
                             "-": 0}
        self.SMS_KEYS = invert_dict(self.SMS_KEYBOARD)
        self.wb = Woordenboek()

    def word_2_sms(self, word) -> str:
        """Translates a word to an sms number"""
        return ''.join([str(self.SMS_KEYBOARD[x]) for x in word.upper()])

    def sms_2_word(self, number) -> list:
        """Gestimate of the possible words based on the T9 number code of an sms

        The gestimate is based on the Woordenboek dictionary so actually quite accurate.
        """
        perms = [''.join(item) for item in itertools.product(*[self.SMS_KEYS[int(x)] for x in str(number)])]
        words = [wrd for wrd in perms if self.wb.is_word(wrd)]
        return words

    def txt_2_sms(self, txt) -> str:
        """
# Text 2 SMS keyboard code

This function translates text to the sms key code equivalent. (T9 keyboard)
        """
        words = txt.split(" ")
        return ' '.join([self.word_2_sms(x.strip()) for x in words])

    def sms_2_txt(self, sms) -> str:
        """
# SMS to Text

This function tries to translate sms key code back to text. This is more difficult a T9 keyboard can have multiple letters
assigned to 1 key, so a dictionary is used to find viable words.

Currently only the Dutch language is supported.

The returned string is a string with per word all the possible solutions in there, so some "manual" decryption might
still be needed.
        """
        numbers = sms.split(" ")
        words = [self.sms_2_word(x) for x in numbers]
        ret = ""
        for wrd in words:
            if len(wrd) == 1:
                ret += wrd[0]
            else:
                ret += "/".join(wrd)
            ret += " "
        return ret


if __name__ == '__main__':
    sms = Sms()
    print(sms.sms_2_word(42556))  # HALLO
    print(sms.sms_2_word(sms.word_2_sms("wereldbol")))
    print(sms.sms_2_word(sms.word_2_sms("wereldburger")))
    print(sms.sms_2_word(sms.word_2_sms("politica")))
    print(sms.txt_2_sms("Deze wereldburger is net zo gemeen als een krokodil"))
    print(sms.sms_2_txt(sms.txt_2_sms("Deze wereldburger is net zo gemeen als een krokodil")))
