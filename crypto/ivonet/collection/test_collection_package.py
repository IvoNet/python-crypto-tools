#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from unittest import main, TestCase

import numpy as np

from ivonet.collection.array import filter_array, flatten_np_array
from ivonet.collection.list import list2dict, list2string, most_common, unique, sort_list_by_another_list, \
    filter_none_from_frequency_count, frequency_count2occurrence_list, increment_smallest


class TestList2Dict(TestCase):
    def gw(self, a, e):
        r = list2dict(a)
        self.assertDictEqual(r, e)

    def test_gw_01(self):
        a = ['a', 'c', 'b']
        e = {'a': 0, 'b': 2, 'c': 1}
        self.gw(a, e)

    def test_gw_02(self):
        a = [1, 2, 3]
        e = {1: 0, 2: 1, 3: 2}
        self.gw(a, e)

    def test_gw_03(self):
        a = np.array([1, 2, 3])
        e = {1: 0, 2: 1, 3: 2}
        self.gw(a, e)

    def test_bw_01(self):
        with self.assertRaisesRegex(AssertionError, 'list'):
            a = 4
            list2dict(a)

    def test_bw_02(self):
        with self.assertRaisesRegex(AssertionError, 'list'):
            a = {1, 2, 3}
            list2dict(a)

    def test_bw_03(self):
        with self.assertRaisesRegex(AssertionError, 'list'):
            a = {1: 0, 2: 1, 3: 2}
            list2dict(a)


class TestList2String(TestCase):
    def gw(self, a, e, sep=None):
        if sep is None:
            r = list2string(a)
        else:
            r = list2string(a, sep)
        self.assertEqual(r, e)

    def test_gw_01(self):
        a = ['a', 'c', 'b']
        e = 'a | c | b'
        self.gw(a, e)

    def test_gw_02(self):
        a = ['a', None, 'b']
        e = 'a | b'
        self.gw(a, e)

    def test_gw_03(self):
        a = ['a', 1, 'b']
        e = 'a | 1 | b'
        self.gw(a, e)

    def test_gw_04(self):
        a = ['a', '', 'b']
        e = 'a | b'
        self.gw(a, e)

    def test_gw_05(self):
        a = ['a', 'c', 'b']
        sep = '-'
        e = 'a-c-b'
        self.gw(a, e, sep)


class TestMostCommon(TestCase):
    def gw(self, a, e):
        r = most_common(a)
        self.assertEqual(r, e)

    def test_gw_01(self):
        a = [0, 1, 1]
        e = 1
        self.gw(a, e)

    def test_gw_02(self):
        a = [0, 1, 1, 0]
        e = 0
        self.gw(a, e)

    def test_gw_03(self):
        a = np.array(['a', 'b', 'b', 'a'])
        e = 'a'
        self.gw(a, e)

    def test_gw_04(self):
        a = {0: 10, 1: 10, 2: 10}.keys()
        e = 0
        self.gw(a, e)

    def test_gw_05(self):
        a = {0: 10, 1: 10, 2: 10}.values()
        e = 10
        self.gw(a, e)

    def test_gw_06(self):
        a = 'abbc'
        e = 'b'
        self.gw(a, e)

    def test_gw_07(self):
        a = 'a'
        e = 'a'
        self.gw(a, e)

    def test_bw_01(self):
        """Verify that an error is raised if the input is no list."""
        with self.assertRaises(AssertionError):
            a = 1
            most_common(a)


class TestUnique(TestCase):
    def gw(self, a, e):
        r = unique(a)
        self.assertListEqual(r, e)

    def bw(self, a):
        with self.assertRaises(AssertionError):
            unique(a)

    def test_gw_01(self):
        a = [0, 0, 1, 1, 4, 3, 2, 4, 2, 3]
        e = [0, 1, 4, 3, 2]
        self.gw(a, e)

    def test_gw_02(self):
        a = np.array([0, 0, 1, 1, 4, 3, 2, 4, 2, 3])
        e = [0, 1, 4, 3, 2]
        self.gw(a, e)

    def test_gw_03(self):
        a = (0, 0, 1, 1, 4, 3, 2, 4, 2, 3)
        e = [0, 1, 4, 3, 2]
        self.gw(a, e)

    def test_gw_04(self):
        a = {0: 0, 1: 10, 2: 10}.keys()
        e = [0, 1, 2]
        self.gw(a, e)

    def test_gw_05(self):
        a = {0: 0, 1: 10, 2: 10}.values()
        e = [0, 10]
        self.gw(a, e)

    def test_bw_01(self):
        """Verify that an error is raised if the input is no list."""
        a = 1
        self.bw(a)


class TestSortListByAnotherList(TestCase):
    def test_gw_01(self):
        lst_a = ['a', 'b', 'c', 'd', 'e']
        lst_b = [0, 0, 3, 2, 0]
        r = sort_list_by_another_list(lst_a, lst_b, reverse=False)
        e = ['a', 'b', 'e', 'd', 'c']
        self.assertListEqual(r, e)

    def test_gw_02(self):
        lst_a = ['a', 'b', 'c', 'd', 'e']
        lst_b = [0, 0, 3, 2, 0]
        r = sort_list_by_another_list(lst_a, lst_b, reverse=True)
        e = ['c', 'd', 'a', 'b', 'e']
        self.assertListEqual(r, e)

    def test_gw_03(self):
        """Verify that empty lists do not raise an exception."""
        lst_a = []
        lst_b = []
        r = sort_list_by_another_list(lst_a, lst_b, reverse=False)
        e = []
        self.assertListEqual(r, e)


class TestFilterArray(TestCase):
    def gw(self, a, e):
        r = filter_array(a)
        #TestUtils.equal_list(self, r, e)
        self.assertEqual(set(r), set(e))

    def test_gw_01(self):
        a = [1, 2, 3, np.nan]
        e = [1, 2, 3]
        self.gw(a, e)

    def test_gw_02(self):
        a = ['a', 'b', 'c', np.nan]
        e = a
        self.gw(a, e)

    def test_gw_03(self):
        a = np.array([1, 2, 3, np.nan])
        e = np.array([1, 2, 3])
        self.gw(a, e)

    def test_gw_04(self):
        a = np.array(['a', 'b', 'c', np.nan])
        e = a
        self.gw(a, e)

    def test_gw_05(self):
        a = [2 ** 0.5, np.nan, 3 ** 0.5, np.nan]
        e = [2 ** 0.5, 3 ** 0.5]
        self.gw(a, e)

    def test_gw_06(self):
        a = np.array([2 ** 0.5, np.nan, 3 ** 0.5, np.nan])
        e = np.array([2 ** 0.5, 3 ** 0.5])
        self.gw(a, e)


class TestFlattenNumpyArray(TestCase):
    def gw(self, a, e):
        r = flatten_np_array(a)
        self.assertEqual(set(r), set(e))

    def test_gw_01(self):
        a = np.array([1, 2, 3, 4, 2, 3, 4])
        e = np.array([1, 2, 3, 4, 2, 3, 4])
        self.gw(a, e)

    def test_gw_02(self):
        a = np.array([[1], [2, 3, 4], [], [2, 3, 4]])
        e = np.array([1, 2, 3, 4, 2, 3, 4])
        self.gw(a, e)

    def test_gw_03(self):
        a = [[1], [2, 3, 4], [], [2, 3, 4]]
        e = np.array([1, 2, 3, 4, 2, 3, 4])
        self.gw(a, e)


class TestIncrementSmallest(TestCase):
    def gw(self, lst, dx, e):
        """Verify that the smallest element is incremented."""
        increment_smallest(lst, dx)
        self.assertListEqual(list(lst), list(e))

    def test_gw_01(self):
        lst_a = np.array([10, 20, 30, 40])
        dx = 5
        e = np.array([15, 20, 30, 40])
        self.gw(lst_a, dx, e)

    def test_gw_02(self):
        lst_a = np.array([50, 20, 30, 40])
        dx = 5
        e = np.array([50, 25, 30, 40])
        self.gw(lst_a, dx, e)

    def test_gw_03(self):
        lst_a = np.array([50, 20, 20, 40])
        dx = 5
        e = np.array([50, 25, 20, 40])
        self.gw(lst_a, dx, e)


class TestFrequencyCount2OccurrenceList(TestCase):
    def gw(self, a, e):
        """Verify that a frequency count can be converted into an occurrence list."""
        r = frequency_count2occurrence_list(a)
        self.assertEqual(list(r), list(e))

    def test_gw_01(self):
        a = [[0, 4], [1, 2], [2, 3], [10, 1]]
        e = np.array([0, 0, 0, 0, 1, 1, 2, 2, 2, 10])
        self.gw(a, e)

    def test_gw_02(self):
        a = [['a', 4], ['b', 2], ['c', 3], ['d', 1]]
        e = np.array(['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd'])
        self.gw(a, e)

    def test_gw_03(self):
        a = [[None, 1], ['a', 4], ['b', 2], ['c', 3], ['d', 1]]
        e = np.array(['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd'])
        self.gw(a, e)

    def test_gw_04(self):
        a = [[None, 1], [1.0, 4], [2, 2], [3.14159265359, 3], ['d', 1]]
        e = np.array(['1.0', '1.0', '1.0', '1.0', '2.0', '2.0',
                      '3.14159265359', '3.14159265359', '3.14159265359', 'd'])
        self.gw(a, e)


class TestFilterNoneFromFrequencyCount(TestCase):
    def gw(self, a, e):
        """Verify that None rows are filtered out a frequency count."""
        r = filter_none_from_frequency_count(a)
        self.assertEqual(r, e)

    def test_gw_01(self):
        a = [[0, 4], [1, 2], [2, 3], [10, 1]]
        e = a
        self.gw(a, e)

    def test_gw_02(self):
        a = [[None, 512], [0, 4], [1, 2], [2, 3], [10, 1]]
        e = [[0, 4], [1, 2], [2, 3], [10, 1]]
        self.gw(a, e)

    def test_gw_03(self):
        a = [[None, 512], ['a', 4], ['b', 2], ['c', 3], ['NULL', 1], ['None', 10]]
        e = [['a', 4], ['b', 2], ['c', 3], ['NULL', 1], ['None', 10]]
        self.gw(a, e)


if __name__ == '__main__':
    main()
