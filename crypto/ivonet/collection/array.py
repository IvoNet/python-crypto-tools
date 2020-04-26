#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import numpy as np

from ivonet.type import Assert


def filter_array(lst):
    """
    Filter out NaN values from a list or np.array.

    If the type of the input list implements np.isnan, filter out NaN.
    Otherwise, leave the input list unaltered.

    Example
    -------
    >> L = [1, 2, 3, np.nan]
    >> UtilsContainer.filter_array(L)
    [1, 2, 3]
    >> L = np.array(['a', 'b', 'c', np.nan])
    >> UtilsContainer.filter_array(L)
    ['a', 'b', 'c', np.nan]
    """

    Assert.seq(lst)

    try:
        lst_invalid = np.isnan(lst)
    except TypeError:
        lst_invalid = np.zeros_like(lst, dtype=bool)
    lst_valid = np.logical_not(lst_invalid)

    if isinstance(lst, list):
        result = list(lst[i] for i in range(len(lst_valid)) if lst_valid[i])
    elif isinstance(lst, np.ndarray):
        result = lst[lst_valid]
    else:
        msg = 'Input shall be either list or numpy array, is now a {}'.format(type(lst))
        raise AssertionError(msg)

    assert type(lst) == type(result)
    return result


def flatten_np_array(lst):
    """Return an np.array with all elements from all sublists in a list or np.array.

    Note: this does not work for nested sublists!

    Returns
    -------
    flat_array: np.array

    Example
    -------
    >> L = np.array([ [1], [2, 3, 4], [], [2, 3, 4] ])
    >> UtilsContainer.flatten_np_array(L)
    [1  2  3  4  2  3  4]
    """

    flat_array = np.array([a for x in lst for a in (x if isinstance(x, list) else [x])])
    return flat_array
