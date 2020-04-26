#!/usr/bin/env python
#  -*- coding: utf-8 -*-

__doc__ = """A word search solver"""
from collections import namedtuple
from itertools import product


class WrongDataException(Exception):
    pass


Direction = namedtuple('Direction', 'di dj name')


class Woordzoeker(object):
    DIRECTIONS = [
        Direction(-1, -1, "up and to the left"),
        Direction(-1, 0, "up"),
        Direction(-1, +1, "up and to the right"),
        Direction(0, -1, "left"),
        Direction(0, +1, "right"),
        Direction(+1, -1, "down and to the left"),
        Direction(+1, 0, "down"),
        Direction(+1, +1, "down and to the right"),
    ]

    def __init__(self, text) -> None:
        self.text = text
        self.grid = []
        self.x = None
        self.y = None
        self.__process()

    def __process(self):
        if not self.text:
            raise WrongDataException("No text provided to create a woordzoeker matrix from.")
        self.grid = [list(x) for x in self.text.split("\n")]
        self.y = len(self.grid)
        if not self.y:
            raise WrongDataException("Could not create a matrix from the provided text.")
        for line in self.grid:
            if not self.x:
                self.x = len(line)
            else:
                if self.x != len(line):
                    raise WrongDataException(
                        "All line lengths in the provided text should be the same: " + "".join(line))
        if not self.x:
            raise WrongDataException("It seems the provided text has no depth...")

    def __str__(self) -> str:
        print()
        ret = "   "
        for i in range(self.x // 10):
            ret += "{:>20}".format(i + 1)
        ret += "\n    "
        for i in range(1, self.x + 1):
            ret += "%s " % (i % 10)
        ret += "\n   +"
        ret += "-" * (self.x * 2 - 1)
        ret += "+\n"
        idx = 0
        for i, line in enumerate(self.grid):
            line_idx = (i + 1) % 10
            if line_idx == 0:
                idx += 1
                line_idx = line_idx + idx * 10
            ret += "%3s|%s|%2s\n" % (line_idx, " ".join(line), line_idx)
        ret += "   +"
        ret += "-" * (self.x * 2 - 1)
        ret += "+\n    "
        for i in range(1, self.x + 1):
            ret += "%s " % (i % 10)
        ret += "\n   "
        for i in range(self.x // 10):
            ret += "{:>20}".format(i + 1)
        return ret + "\n"

    def __extract(self, i, j, direction, length):
        """
        Extract letters from the grid, starting at row i column j, as a string.
        If the extraction will walk out of bounds, return None.
        """
        if (0 <= i + (length - 1) * direction.di < len(self.grid) and
                0 <= j + (length - 1) * direction.dj < len(self.grid[i])):
            return ''.join(
                self.grid[i + n * direction.di][j + n * direction.dj] for n in range(length)
            )
        return None

    def search(self, word):
        """
        Search for a word in a grid, returning a tuple of the starting row,
        starting column, and direction.  If the word is not found, return None.

        will return the zero indexed values
        """
        word_len = len(word)
        for i, j, direction in product(range(len(self.grid)), range(len(self.grid[0])), self.DIRECTIONS):
            if word == self.__extract(i, j, direction, word_len):
                return i, j, direction
        return None

    def search_as_text(self, word) -> str:
        """
        Same as search() but will return the 1 indexed values as a readable string
        :return: one indexed readable string of search result
        """
        match = self.search(word.upper())
        if match is None:
            return "Didn't find a match for: {0}".format(word)
        else:
            i, j, direction = match
            return "Found a match for {0} at line {1}, column {2} going {3}".format(word, i + 1, j + 1, direction.name)

    def print(self, word) -> None:
        """
        Same as search_as_text
        """
        print(self.search_as_text(word))


class WordFinder(Woordzoeker):
    """
    English version of Woorzoeker :-)
    """
    pass


if __name__ == '__main__':
    MATRIX_NO_SPACE = """MULTIVIBRATORSHROAOOTABOFA ZIJN# #E
LEK#T##R#ONOEEAFAESSVRUMNISC#HE SL#
NCH#AKEL##INGFYCGSBHTLEN. D#E EEXDR
SEBMOFPLVHOSASWCTVIAMSQCCRNCE MUEIN
LTOUIVIBRATFRECVORSRGRXAAGG#ORG WYW
SCHRGAKCEPMTDPMDFERMSLELINL##OPGEXE
 WDEONR#ND IINF 1918# ONTFNEWIYIWNR
KKXELKIBDQ DAIONOR HENREIEAF#DDBAMA
F#G ABMWRRRAHNRAUM #EN KERIT#WMHOAM
UUPRGFTFDASAE#RVNCE BLOI#KEEIMAOAFE
VCSHOLVSDNPQO.#HK ELATERRNFLCPIDNGG
D CAGOPRXNIDSO#DYZFQAT W#SIVLOYHWLN
A#QQPJAAAMOMFTSAAEAHSR#B BCEBDYAIIA
KTPSNONNZSKTHQACWIHREMKRKDHSAAHVHOE
LCDNNELDEOLNEBEXSN CBEOIEACQZXSVCAV
TDBCXCNCLEFIAENABLVREIOLSN MQNRD#RN
NLASMEYENXVSOX ELAGIDGRRJDOBIRGRDCF
OVUSRGLANN CGENDVTONXAOPGE YQBFTISN
CNKMGWCTASBIMLAELIERWKGPCO EI#ODAMU
REUNRBLLTAIVIMIKBRI#EFMMNEFNATIYEOM
NE#TSBMR.K D#IAT ONETBIQOWAHEROSGPY
VT LESPWEARD OAUVUERDLPFLENNDESOISD
NIRKAWFMEO#ER WLRKXBIIQVKRGGEBXXLCK
SFRUFDBORICRAAGOAMNU#IK#CTLS IIORNN
QA CTARDE KHDEOECDNFHCOLOVSLHSUYHE#
AS IOFIWAANDFVOSYEFQQAIFRUFMOREEIOE
 DUWQSITS BERI#FGWLSLDEXCSCLHBAQEQT
ENAEOLLMECLFAIGNVER#KEER#O #WEHKXT#
RD ONTQDUCMRDRDNMYGHLCIJFMERD IRLNN
 DEFNIDMHNEBOE TW#DMEWNHVBYIEEDKBK#
E #WESRKAFNSRGSNAPTRZZ#REKLDOORVLIO
G. WAT IS ##HNVDDAALFMNLCSOABMSD#TE
 P#OP#AXIDNIAANMNRNVRMLAULAI#RE NA#
LZIOLTOIBRIAM VA#NTUIDCAUSRRCSER# D
EZE SKDRHIDIENCLGCHTLGACH#AKELIN#G?"""
    wz = Woordzoeker(MATRIX_NO_SPACE)
    print(wz)
    wz.print("DMAL")
    wz.print("MULTIVIBRATORS")
