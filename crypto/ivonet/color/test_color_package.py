#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from unittest import TestCase, main

from ivonet.color.rgb import hsb2rgb


class TestHsb2Rgb(TestCase):
    def gw(self, hsb, e):
        """Verify that a hsb value is properly transformed into a rgb value"""
        r = hsb2rgb(hsb)
        self.assertListEqual(list(r), list(e))

    def test_gw_01(self):
        hsb = (0, 100, 100)
        e = [255, 0, 0]
        self.gw(hsb, e)

    def test_gw_02(self):
        hsb = (180, 100, 100)
        e = [0, 255, 255]
        self.gw(hsb, e)

    def test_gw_03(self):
        hsb = (90, 50, 50)
        e = [96, 128, 64]
        self.gw(hsb, e)

    def test_gw_04(self):
        hsb = (270, 0, 50)
        e = [128, 128, 128]
        self.gw(hsb, e)

    def test_gw_05(self):
        hsb = (270, 50, 0)
        e = [0, 0, 0]
        self.gw(hsb, e)

    def test_gw_06(self):
        hsb = (0, 0, 100)
        e = [255, 255, 255]
        self.gw(hsb, e)


if __name__ == '__main__':
    main()
