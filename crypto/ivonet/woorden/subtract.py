#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from ivonet.string.alphabet import alphabet_loc, alphabet_idx


def word_minus_word(links, rechts):
    """ (see opgave 11 kerstpuzzel 2020)

    :param links: word left of equation
    :param rechts: word right of equation
    :return: left - right
    """
    ret = ""
    suffix = ""
    loop = len(links)
    if len(links) > len(rechts):
        for letter in links[len(rechts):]:
            suffix += " " + letter.upper()
            loop = len(rechts)
    if len(links) < len(rechts):
        for letter in rechts[len(links):]:
            suffix += " -" + letter

    for il, ll in enumerate(links[:loop], start=0):
        lr = rechts[il]
        pl = alphabet_loc(ll)
        pr = alphabet_loc(lr)
        if pl < pr:
            ret += " -"
            ret += alphabet_idx(abs(alphabet_loc(ll, indexed=1) - alphabet_loc(lr, indexed=0))).upper()
        elif pl == pr:
            ret += " *"
        else:  # pl > pr
            ret += " " + alphabet_idx(abs(alphabet_loc(ll, indexed=0) - alphabet_loc(lr, indexed=1))).upper()
    ret = ret + suffix
    if ret.startswith(" "):
        return ret[1:].upper()
    return ret.upper()
