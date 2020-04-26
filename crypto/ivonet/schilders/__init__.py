#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import os


# http://kunst-schilder.blogspot.nl/search/label/LIJST%20ALFABET%20HOLLANDSE%20SCHILDERS
# http://kunst-schilder.blogspot.nl/2015/04/normal-0-21-false-false-false-nl-x-none.html

def _get_file(fi):
    return open(os.path.join(os.path.split(__file__)[0], fi), "r").read().strip().lower().split("\n")


class Schilder(object):
    def __init__(self, record):
        self.naam = None
        self.geboorte_jaar = None
        self.overlijden_jaar = None
        self.geboorte_plaats = None
        self.overlijden_plaats = None
        record.split("")
