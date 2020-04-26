#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from ivonet.games.kaarten import kaart_soorten
from ivonet.string import pretty_print


def aap_noot_mies_india():
    return (
        "jaap",
        "gijs",
        "dien",
        "zus",
        "boe",
        "oom",
        "waf",
        "vuur",
        "rook",
        "tol",
        "zeil",
        "de neus",
        "het huis",
        "een schip"
    )


def aap_noot_mies():
    return (
        "aap",
        "noot",
        "mies",
        "wim",
        "zus",
        "jet",
        "teun",
        "vuur",
        "gijs",
        "lam",
        "kees",
        "bok",
        "weide",
        "does",
        "hok",
        "duif",
        "schapen",
    )


def alpha_beta_gamma() -> tuple:
    return (("alfa", "alpha", "\u03B1", "\u0391"),
            ("bèta", "beta", "\u03B2", "\u0392"),
            ("gamma", "gamma", "\u03B3", "\u0393"),
            ("delta", "delta", "\u03B4", "\u0394"),
            ("epsilon", "epsilon", "\u03B5", "\u0395"),
            ("zèta", "zeta", "\u03B6", "\u0396"),
            ("èta", "eta", "\u03B7", "\u0397"),
            ("thèta", "theta", "\u03B8", "\u0398"),
            ("jota", "iota", "\u03B9", "\u0399"),
            ("kappa", "kappa", "\u03BA", "\u039A"),
            ("lambda", "lambda", "\u03BB", "\u039B"),
            ("mu", "mu", "\u03BC", "\u039C"),
            ("nu", "nu", "\u03BD", "\u039D"),
            ("xi", "xi", "\u03BE", "\u039E"),
            ("omikron", "omicron", "\u03BF", "\u039F"),
            ("pi", "pi", "\u03C0", "\u03A0"),
            ("rho", "rho", "\u03C1", "\u03A1"),
            ("sigma", "sigma", "\u03C3", "\u03A3"),
            ("tau", "tau", "\u03C4", "\u03A4"),
            ("ypsilon", "upsilon", "\u03C5", "\u03A5"),
            ("phi", "phi", "\u03C6", "\u03A6"),
            ("chi", "chi", "\u03C7", "\u03A7"),
            ("psi", "psi", "\u03C8", "\u03A8"),
            ("omega", "omega", "\u03C9", "\u03A9"))


def nato_alfabet():
    return (("A", "Alfa"),
            ("B", "Bravo"),
            ("C", "Charlie"),
            ("D", "Delta"),
            ("E", "Echo"),
            ("F", "Foxtrot"),
            ("G", "Golf"),
            ("H", "Hotel"),
            ("I", "India"),
            ("J", "Juliett"),
            ("K", "Kilo"),
            ("L", "Lima"),
            ("M", "Mike"),
            ("N", "November"),
            ("O", "Oscar"),
            ("P", "Papa"),
            ("Q", "Quebec"),
            ("R", "Romeo"),
            ("S", "Sierra"),
            ("T", "Tango"),
            ("U", "Uniform"),
            ("V", "Victor"),
            ("W", "Whisky"),
            ("X", "X-ray"),
            ("Y", "Yankee"),
            ("Z", "Zulu")
            )


def planeten():
    return (
        "Mercurius",
        "Venus",
        "Aarde",
        "Mars",
        "Jupiter",
        "Saturnus",
        "Uranus",
        "Neptunus",
        "Pluto",
    )


def dierenriem_nl():
    return (("Aries", "Ram", "21 maart"),
            ("Taurus", "Stier", "20 april"),
            ("Gemini", "Tweelingen", "21 mei"),
            ("Cancer", "Kreeft", "21 juni"),
            ("Leo", "Leeuw", "23 juli"),
            ("Virgo", "Maagd", "23 augustus"),
            ("Libra", "Weegschaal", "23 september"),
            ("Scorpius", "Schorpioen", "23 oktober"),
            ("Sagittarius", "Boogschutter", "22 november"),
            ("Capricornus", "Steenbok", "22 december"),
            ("Aquarius", "Waterman", "20 januari"),
            ("Pisces", "Vissen", "19 februari"),)


def dierenriem_china():
    return ("Rat",
            "Os",
            "Tijger",
            "Konijn",
            "Draak",
            "Slang",
            "Paard",
            "Geit",
            "Aap",
            "Haan",
            "Hond",
            "Varken")


def premiers():
    return (
        ("Willem Schermerhorn", "*17 december 1894", "✝10 maart 1977",),
        ("Louis Beel", "*12 april 1902", "✝11 februari 1977",),
        ("Willem Drees", "*15 juli 1886", "✝14 mei 1988",),
        ("Louis Beel", "*12 april 1902", "✝11 februari 1977",),
        ("Jan de Quay", "*26 augustus 1901", "✝4 juli 1985",),
        ("Victor Marijnen", "*21 februari 1917", "✝5 april 1975",),
        ("Jo Cals", "*18 juli 1914", "✝30 december 1971",),
        ("Jelle Zijlstra", "*27 augustus 1918", "✝23 december 2001",),
        ("Piet de Jong", "*3 april 1915", "✝27 juli 2016",),
        ("Barend Biesheuvel", "*5 april 1920", "✝29 april 2001",),
        ("Joop den Uyl", "*9 augustus 1919", "✝24 december 1987",),
        ("Dries van Agt", "*2 februari 1931", "✝-",),
        ("Ruud Lubbers", "*7 mei 1939", "✝14 februari 2018",),
        ("Wim Kok", "*29 september 1938", "✝20 oktober 2018",),
        ("Jan Peter Balkenende", "*7 mei 1956", "✝-",),
        ("Mark Rutte", "*14 februari 1967", "✝-",),
    )


def twaalf_apolstelen():
    return ("Andreas",
            "Bartolomeüs",
            "Filippus",
            "Jakobus",
            "Jakobus de Meerdere",
            "Johannes",
            "Judas Taddeüs",
            "Matteüs",
            "Mattias",
            "Simon Petrus",
            "Simon",
            "Thomas",)


def seizoenen():
    return "HERFST", "LENTE", "WINTER", "ZOMER"


def windrichtingen():
    return "NOORD", "OOST", "WEST", "ZUID"


def smaken():
    return "BITTER", "ZOET", "ZOUT", "ZUUR"


def elementen():
    return "AARDE", "LUCHT", "VUUR", "WATER"


def regenboog():
    return "ROOD", "ORANJE", "GEEL", "GROEN", "BLAUW", "PAARS/INDIGO", "VIOLET"


def snowwwhite_zeven_dwarfs():
    return "BASHFULL", "DOC", "DOPEY", "GRUMPY", "HAPPY", "SLEEPY", "SNEEZY"


if __name__ == '__main__':
    pretty_print(aap_noot_mies_india())
    pretty_print(aap_noot_mies())
    pretty_print(planeten())
    pretty_print(alpha_beta_gamma())
    pretty_print(dierenriem_nl())
    pretty_print(dierenriem_china())
    pretty_print(premiers())
    pretty_print(twaalf_apolstelen())
    pretty_print(windrichtingen())
    pretty_print(smaken())
    pretty_print(elementen())
    pretty_print(kaart_soorten())
    pretty_print(regenboog())
    pretty_print(nato_alfabet())
