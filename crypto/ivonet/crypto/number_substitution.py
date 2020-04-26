#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from ivonet.crypto.key_word_substitution import KeyWordSubstitution
from ivonet.string.alphabet import alphabet

__doc__ = """
This module does simple substitution on text based an a alphabet and indexing
"""

DEFAULT_ALPHABET = (" " + alphabet()).upper()


def numbers_to_text(number, alpha=DEFAULT_ALPHABET):
    """
# Numbers 2 text

This function translates via number substitution a number to text.
This is a very fragile function as it will only work in certain cases.
    """
    return "".join([alpha[int(x)] for x in number])


def text_to_numbers(text, alpha=DEFAULT_ALPHABET):
    """
# Text 2 numbers

Function to translate text to numbers via number substitution.

Find the index of the letter in the alphabet to find the number.
    """
    return "".join([str(alpha.index(x)) for x in text.upper()])


def numbers_to_text_by_keyword(number, keyword):
    kws = KeyWordSubstitution(keyword)
    alpha = " " + kws.get_permutation_alphabet()
    return numbers_to_text(number, alpha)


def text_to_numbers_by_keyword(text, keyword):
    kws = KeyWordSubstitution(keyword)
    alpha = " " + kws.get_permutation_alphabet()
    return text_to_numbers(text, alpha)


if __name__ == '__main__':
    TXT = "DE GEDAAGDE BAGAGEDIEF GAF DE BEEDIGDE CHEF DE ACACIA"
    print(TXT, text_to_numbers(TXT), numbers_to_text(text_to_numbers(TXT)))
    KEY = "kerstpuzzel"
    TXT = "ELKE KLEUTER PEUZELT REUZELEKKERE LEPELS REUZEL"
    print(TXT, text_to_numbers_by_keyword(TXT, KEY),
          numbers_to_text_by_keyword(text_to_numbers_by_keyword(TXT, KEY), KEY))
    TXT = "Deze tekst gaat fout"
    print(TXT, text_to_numbers(TXT), numbers_to_text(text_to_numbers(TXT)))
