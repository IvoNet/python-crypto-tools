#!/usr/bin/env python
#  -*- coding: utf-8 -*-

DEBUG = False


def _(*args, end="\n"):
    if DEBUG:
        print(*args, end=end)
