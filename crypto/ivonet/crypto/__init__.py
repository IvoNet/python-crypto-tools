#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import hashlib


def md5(source_string):
    encoded_string = source_string.encode(encoding='utf_8', errors='strict')
    hashed_string = hashlib.md5(encoded_string)
    result = hashed_string.hexdigest()
    return result
