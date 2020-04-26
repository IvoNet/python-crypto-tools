#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from ivonet.log import _
from ivonet.woorden.woordenboek import Woordenboek

__doc__ = """

# Gegeven 

een string als deze

HCIALWTLAVMNSSRTECCTISRAENAVUEAETAANROAN
or
HALLOWERELDWIJZIJNMENSENMETHETGROTEGELUK

# Doel

- Vind de zin en durf te zeggen dat we het zijn

# regels

- kijk vanaf het begin van de zin en zie hoe lang je een woord kan maken
- Bewaar elk woord dat je vind vanaf 2 letters
- dit is geen garantie dat je het juiste woord hebt maar het is een start
- begin met het langste woord
- als niks gevonden dan ben je klaar met die iteratie
- voor elk woord herhaal bovenstaande met het woord er af gehaald to to niks over is.

voorbeeld:

HALLOWERELDWIJZIJNMENSENMETHETGROTEGELUK

het eerste woord dat je mogelijk vind is HA, maar ook HAL en HALLO voordat je geen woord meer kan vinden
Stel jdat je met het langste woord begint dan kan je opnieuw beginnen op met HALLO er van af gehaald, maar je
hebt ook de woorden (HA, HAL) bewaard. nu begin je opnieuw op de positie na HALLO. we vinden dan bijvoorbeeld
(WE, en WERELD) begin weer bij het langste woord en ga zo door. 
Stel dat het na WERELD faalt (geen woorden meer) dan val je terug op WE en ga je weer verder totdat alles faalt
en dan kan je nog terug vallen op HAL en weer opnieuw beginnen en HA etc.
Het enige gelukkige pad is als alle 40 karakters gebruikt zijn in woorden.

"""

WB = Woordenboek()


class NotFound(Exception):
    pass


class Found(Exception):

    def __init__(self, msg) -> None:
        self.value = msg


class StringWordAnalyser(object):

    def __init__(self, value="") -> None:
        self.wb = Woordenboek()
        self.sample = value

    def all_words(self, value) -> bool:
        self.sample = value
        try:
            self.__all_words()
        except NotFound:
            _("Sample was not a sentence")
            return False
        except Found as f:
            _("Found: ", f.value)
            return True

    def __all_words(self, value=None):
        if value:
            ret = value
        else:
            ret = self.sample

        for idx in range(len(ret), 1, -1):
            wrd = ret[0:idx]
            if self.wb.is_word(wrd):
                _(wrd)
                new_wrd = ret[idx:]
                if len(new_wrd) == 0:
                    _(self.sample)
                    raise Found(self.sample)
                self.__all_words(new_wrd)
            else:
                _(idx, wrd)
                if idx == 2:
                    raise NotFound()


