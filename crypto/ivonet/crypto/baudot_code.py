#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from ivonet.collection.dictinary import reverse_dict

#TODO can be expanded upon
# https://en.wikipedia.org/wiki/Baudot_code
# https://nl.wikipedia.org/wiki/Baudotcode#De_oorspronkelijke_Baudotcode_(CCITT-1)


BAUDOT_ALPHABET = {
    "A": "10000",
    "B": "00110",
    "C": "10110",
    "D": "11110",
    "E": "01000",
    "F": "01110",
    "G": "01010",
    "H": "11010",
    "I": "01100",
    "J": "10010",
    "K": "10011",
    "L": "11011",
    "M": "01011",
    "N": "01111",
    "O": "11100",
    "P": "11111",
    "Q": "10111",
    "R": "00111",
    "S": "00101",
    "T": "10101",
    "U": "10100",
    "V": "11101",
    "W": "01101",
    "X": "01001",
    "Y": "00100",
    "Z": "11001",
    ".": "10001",
    "*": "00011",
    "_": "00010",
    " ": "00001",
    "-": "00000",
}

ALPHABET_BAUDOT = reverse_dict(BAUDOT_ALPHABET)


def text_2_baudot(txt, delimiter=" ") -> str:
    """
# Text 2 Baudot code

This function will translate standard text to the [Baudotcode](https://nl.wikipedia.org/wiki/Baudotcode).
    """
    answer = ""
    for x in txt.upper():
        answer += BAUDOT_ALPHABET[x]
        answer += delimiter
    return answer


def baudot_2_text(baudot, delimiter=" ") -> str:
    """
# TBaudot code 2 Text

This function will translate the [Baudotcode](https://nl.wikipedia.org/wiki/Baudotcode) encoded text to standard text.
    """
    answer = ""
    for x in baudot.strip().split(delimiter):
        answer += ALPHABET_BAUDOT[x]
    return answer
