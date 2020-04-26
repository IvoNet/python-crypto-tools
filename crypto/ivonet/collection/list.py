#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import itertools
import operator

import numpy as np

from ivonet.type import Assert


def list_equal(lst) -> bool:
    """checks if all elements in list are equal"""
    return not lst or lst.count(lst[0]) == len(lst)


def pairwize(singlelist):
    """Creates a paired list from a list of values

    e.g. [1, 2, 3, 4, 5]
    gives an iterator that returns:
    (1, 2)
    (3, 4)
    The 5 is gone
    """
    return zip(singlelist[::2], singlelist[1::2])


def pairwize_as_list(singlelist):
    """same as pairwize but returns a list iso an iter"""
    return [x for x in pairwize(singlelist)]


def rotate(value, left=1):
    """Left shift or rotate a list by 'left' value"""
    if left == 0:
        return value
    return value[left:] + value[:left]


def list2dict(lst):
    """
    Convert a list to a dictionary, where the key of each entry are the list
    elements, and the values are indices 0..N, where the ordering is the ordering
    used in the list.
    """
    Assert.seq(lst)
    nr_elements = len(lst)
    result = dict(zip(lst, range(nr_elements)))

    assert isinstance(result, dict), 'Output shall be a dictionary'
    msg = 'All elements of input list ({}) shall be in dictionary ({})'.format(len(result), len(lst))
    assert len(result) == len(lst), msg
    return result


def list2string(lst, separator=" | "):
    """Concatenate all string values in a list.

    Empty strings are left out
        """
    lst = remove_none_from_list(lst)
    lst = [str(x) for x in lst if x != '']
    return separator.join(lst)


def remove_none_from_list(lst):
    """Filter out all None values from a list."""
    return list(filter(None.__ne__, lst))


def most_common(lst):
    """
    Return the most common element in a list.
    In case of a draw, the element that appears first in the list is selected.
    """

    try:
        # Get an iterable of (item, iterable) pairs
        sorted_list = sorted((x, i) for i, x in enumerate(lst))
        groups = itertools.groupby(sorted_list, key=operator.itemgetter(0))

        # Auxiliary function to get "quality" for an item
        def _auxfun(g):
            _, iterable = g
            count = 0
            min_index = len(lst)
            for _, where in iterable:
                count += 1
                min_index = min(min_index, where)
            return count, -min_index

        # Pick the highest-count/earliest item
        return max(groups, key=_auxfun)[0]
    except TypeError:
        msg = 'Input to most_common shall be an iterable.\n'
        msg += 'Type of L: {0}\n'.format(type(lst))
        raise AssertionError(msg)


def unique_list_of_lists(list_of_lists) -> list:
    """returns the list op lists input as a unique list of list"""
    return [list(x) for x in set(tuple(x) for x in list_of_lists)]


def unique(lst) -> list:
    """
    Given a seq (any iterable object), return the seq with duplicates removed.
    The order of the elements is unchanged.
    """

    try:
        seen = set()
        result = [x for x in lst if not (x in seen or seen.add(x))]
        assert len(result) <= len(lst), 'No elements shall be added'
        return result
    except TypeError:
        msg = 'Input to unique shall be an iterable.\n'
        msg += 'Type of L: {0}\n'.format(type(lst))
        raise AssertionError(msg)


def sort_list_by_another_list(lst_a, lst_b, reverse=False):
    """
    Sort the items in list L by key the items of list M.
    """

    try:
        assert len(lst_a) == len(lst_b), 'Lists L and M shall have equal length'
        result = [x[0] for x in sorted(zip(lst_a, lst_b),
                                       key=operator.itemgetter(1),
                                       reverse=reverse)]
        return result
    except TypeError:
        msg = 'Both inputs to sort_list_by_another_list shall be an iterable.\n'
        msg += 'Type of L: {0}\n'.format(type(lst_a))
        msg += 'Type of M: {0}\n'.format(type(lst_b))
        raise AssertionError(msg)


def increment_smallest(lst, dx):
    """Increment the smallest element of the list L with the given amount dx.

    If the minimum occurs multiple times, the first element is incremented."""

    Assert.py_type(lst, np.ndarray, 'L')

    min_index = np.argmin(lst)
    lst[min_index] += dx


def frequency_count2occurrence_list(frequency_count):
    """Transform a frequency count into an occurrence list.

    A frequency count is a list of tuples or a list of lists, in which the first
    element is the property, and the second element is the count. An occurrence
    list is a list with each property <count> times in it.

    Parameters
    ----------
    frequency_count: list of lists or tuples with length 2

    Returns
    -------
    occurrence_list: np.array, dtype = <type(most general key in frequency_count)>

    Example
    -------
    >> a = [ [0, 4], [1, 2], [2, 3], [10, 1] ]
    >> UtilsContainer.frequency_count2occurrence_list(a)
    [ 0  0  0  0  1  1  2  2  2 10]
    >> a = [ ['a', 4], ['b', 2], ['c', 3], ['d', 1] ]
    >> UtilsContainer.frequency_count2occurrence_list(a)
    ['a' 'a' 'a' 'a' 'b' 'b' 'c' 'c' 'c' 'd']
    """

    Assert.frequency_count(frequency_count)

    occurrence_list = np.empty(0)
    for k, v in frequency_count:
        if k is not None:
            k_list = np.empty(v, dtype=type(k))
            k_list.fill(k)
            occurrence_list = np.append(occurrence_list, k_list)

    return occurrence_list


def filter_none_from_frequency_count(frequency_count):
    """
    Filter out None rows from a frequency count.

    A frequency count is a list of tuples or a list of lists, in which the first
    element is the property, and the second element is the count.

    Parameters
    ----------
    frequency_count: list of lists or tuples with length 2

    Returns
    -------
    new_frequency_count: list of lists or tuples with length 2

    Example
    -------
    >> a = [ [None, 4], [1, 2], [2, 3], [10, 1] ]
    >> UtilsContainer.filter_none_from_frequency_count(a)
    [ [1, 2], [2, 3], [10, 1] ]
    >> a = [ [None, 4], ['None', 2], ['c', 3], ['d', 1] ]
    >> UtilsContainer.filter_none_from_frequency_count(a)
    [ ['None', 2], ['c', 3], ['d', 1] ]
    """

    Assert.frequency_count(frequency_count)

    new_frequency_count = [x for x in frequency_count if x[0] is not None]
    return new_frequency_count


def list_permutations(lst) -> list:
    """Returns all permutations of a given list
    e.g. permutations([1, 2, 3])
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]
    """
    return list(itertools.permutations(list(lst)))


