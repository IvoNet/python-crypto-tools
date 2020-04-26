#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import operator


def sort(dictionary, by_value=False, reverse=False) -> list:
    """Convenience method for sorting a dict as I can never remember it."""
    sort_operator = 1 if by_value else 0
    return sorted(dictionary.items(), key=operator.itemgetter(sort_operator), reverse=reverse)


def sort_by_value(dictionary, reverse=False) -> list:
    """Returns the dictionary sorted by value"""
    return sort(dictionary, by_value=True, reverse=reverse)


def sort_by_key(dictionary, reverse=False) -> list:
    """Returns the dictionary sorted by key"""
    return sort(dictionary, reverse=reverse)


def sort_by_value_then_key(dictionary, reverse=False) -> list:
    """Returns a dictionary as a list sorted first on value then on key"""
    return sorted(dictionary.items(), key=lambda x: (x[1], x[0]), reverse=reverse)


def reverse_dict(dct):
    """Reverse the dictionaty D: keys will be values, values will be keys."""
    nr_unique_values = len(set(dct.values()))
    msg = 'Dictionary does not have a one-to-one relationship'
    assert nr_unique_values == len(dct), msg
    return {dct[k]: k for k in dct}


def invert_dict(dct):
    """Reverse the dictionary. Keys will be [values] and values will be keys"""
    ret = {}
    for value in set(dct.values()):
        ret[value] = []
    for key in dct:
        ret[dct[key]].append(key)
    return ret
