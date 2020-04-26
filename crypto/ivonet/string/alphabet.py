#!/usr/bin/env python
#  -*- coding: utf-8 -*-


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
KLINKERS = "aeiouy"
MEDEKLINKERS = "bcdfghjklmnpqrstvwxz"


def alphabet(upper=False):
    if upper:
        return ALPHABET.upper()
    return ALPHABET


def alphabet_list(upper=False):
    return list(alphabet(True))


def alphabet_idx(idx):
    return ALPHABET[idx]


def alphabet_loc(letter, indexed=1):
    return ALPHABET.index(letter.lower()) + indexed


def letter_values_of_word(word, indexed=1):
    return [alphabet_loc(x, indexed) for x in word]


def sum_letter_values_of_word(word, indexed=1):
    ret = 0
    for x in letter_values_of_word(word, indexed):
        ret += x
    return ret


def product_letter_values_of_word(word, indexed=1) -> int:
    ret = 1
    for x in letter_values_of_word(word, indexed):
        ret *= x
    return ret


def base_26_encode_string(word):
    """Encodes a string to a base 26 encoded number
    A = 0, B = 1, Z = 25, BA = 26, BB = 27, XYZ = 16197
    """
    row = list(word)[::-1]
    num = 0
    for i, x in enumerate(row):
        loc = alphabet_loc(x, indexed=0)
        num = num + loc * 26 ** i
    return num


def is_klinker(letter):
    """True if a klinker"""
    return letter in KLINKERS


def is_medeklinker(letter):
    """True if a medeklinker"""
    return letter in MEDEKLINKERS


def filter_klinkers(txt):
    """Return only the klinkers of the string"""
    return "".join(x for x in txt if is_klinker(x))


def filter_klinker_pos(txt, indexed=0) -> list:
    """Return all the klinkers with their respective position in the txt (indexed)

    e.g [('e', 1), ('a', 8),]
    """
    ret = []
    for i, letter in enumerate(txt):
        if is_klinker(letter):
            ret.append((letter, i + indexed))
    return ret


def filter_medeklinkers(txt):
    """Return only the medeklinkers of the string"""
    return "".join(x for x in txt if is_medeklinker(x))


def filter_medeklinker_pos(txt, indexed=0) -> list:
    """Return all the medeklinkers with their respective position in the txt (indexed)

    e.g [('b', 1), ('l', 8),]"""
    ret = []
    for i, letter in enumerate(txt):
        if is_medeklinker(letter):
            ret.append((letter, i + indexed))
    return ret


def print_alphabet(indexed=1):
    [print("%2s = %s" % (i + indexed, y.upper())) for i, y in enumerate(ALPHABET)]


if __name__ == '__main__':
    print_alphabet()
    print(alphabet_loc("A"))  # 1
    print(filter_klinkers("hallo, Wereld"))
    print(filter_klinker_pos("hallo, Wereld", 1))
    print(filter_medeklinkers("hallo, Wereld"))
