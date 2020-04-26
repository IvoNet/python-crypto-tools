import unittest
from unittest import TestCase

from ivonet.crypto.bifid import bifid_key, pos, bifid_decrypt, bifid_encrypt
from ivonet.crypto.caesar import caesar_cipher
from ivonet.crypto.key_word_substitution import KeyWordSubstitution
from ivonet.crypto.mono_alphabetic_substitution import encryptMessage
from ivonet.crypto.morsecode import text_2_morse, morse_2_text, letters_as_morse_2_text, dna_2_text
from ivonet.crypto.number_substitution import numbers_to_text, text_to_numbers, text_to_numbers_by_keyword, \
    numbers_to_text_by_keyword
from ivonet.crypto.one_time_pad import otp, otp_decrypt, otp_encrypt
from ivonet.crypto.sms import Sms
from ivonet.crypto.tabula_recta import tabula_recta, tabula_recta_decode


class TestKeyWordSubstitution(unittest.TestCase):

    def setUp(self):
        self.kws = KeyWordSubstitution()

    def test_2012_inzending(self):
        self.kws.create_permutation_dict("musketier")
        self.assertEqual("D’ARTAGNAN", self.kws.permute_message("K’MNPMIGMG"))
        self.assertEqual("ARAMIS", self.kws.permute_message("MNMFAO"))
        self.assertEqual("ATHOS", self.kws.permute_message("MPRHO"))
        self.assertEqual("PORTHOS", self.kws.permute_message("JHNPRHO"))

    def test_2013_opgave_2a(self):
        self.kws.create_permutation_dict("STOPLICHTALMELO")
        self.assertEqual(
            "HET STOPLICHT SPRINGT OP ROOD, HET STOPLICHT SPRINGT OP GROEN, IN ALMELO IS ALTIJD WAT TE DOEN – HERMAN FINKERS",
            self.kws.permute_message(
                "HLR QRGJBAOHR QJNAFCR GJ NGGP, HLR QRGJBAOHR QJNAFCR GJ CNGLF, AF SBDLBG AQ SBRAMP WSR RL PGLF – HLNDSF IAFELNQ"))

    def test_2013_opgave_6(self):
        self.kws.create_permutation_dict("GEBROEDERSGRIMM")
        self.assertEqual("ROODKAPJE DUIMENDIK ASSEPOESTER SNEEUWWITJE RAPONSJE",
                         self.kws.permute_message("PKKRCGLAO RUMHOJRMC GQQOLKOQTOP QJOOUWWMTAO PGLKJQAO"))

    def test_2013_opgave_6b(self):
        """Gebazeerd op de lengte van de gebruikte woorden"""
        self.kws.create_permutation_dict("NEGENTIEN")
        self.assertEqual("IDENTIFICATIENUMMER", self.kws.permute_message("DTILSDADGNSDILUKKIQ"))
        self.kws.create_permutation_dict("TWINTIG")
        self.assertEqual("OVERZICHTELIJKSHALVE", self.kws.permute_message("LUGPZDICRGHDEFQCTHUG"))
        self.kws.create_permutation_dict("DRIEENTWINTIG")
        self.assertEqual("RUITENSPROEIERVLOEISTOF", self.kws.permute_message("OSAQNJPLOKNANOUFKNAPQKT"))
        self.kws.create_permutation_dict("VIJFENTWINTIG")
        self.assertEqual("LANGEAFSTANDSBOMMENWERPER", self.kws.permute_message("CVHTEVNPQVHFPIKDDEHUEOLEO"))
        self.kws.create_permutation_dict("ZEVENENTWINTIG")
        self.assertEqual("HOTTENTOTTENTENTOONSTELLING", self.kws.permute_message("GJPPTHPJPPTHPTHPJJHOPTDDAHI"))
        self.kws.create_permutation_dict("DERTIG")
        self.assertEqual("LEVENSVERZEKERINGSMAATSCHAPPIJ", self.kws.permute_message("JIVILQVIPZIHIPCLAQKDDSQRBDNNCF"))
        self.kws.create_permutation_dict("VIERENDERTIG")
        self.assertEqual("SUPERCALIFRAGILISTICEXPIALIDOCIOUS",
                         self.kws.permute_message("PSLNOEVFADOVTAFAPQAENXLAVFARKEAKSP"))

    def test_2014_opgave_3a(self):
        self.kws.create_permutation_dict("LEO VROMAN")
        self.assertEqual(
            "KOM VANAVOND MET VERHALEN HOE DE OORLOG IS VERDWENEN, EN HERHAAL ZE HONDERD MALEN: ALLE MALEN ZAL IK WENEN",
            self.kws.permute_message(
                "DIG ULHLUIHV GRS URPNLFRH NIR VR IIPFIA BQ URPVWRHRH, RH NRPNLLF ZR NIHVRPV GLFRH: LFFR GLFRH ZLF BD WRHRH"))

    def test_2014_opgave_3b(self):
        self.kws.create_permutation_dict("LIBRIS LITERATUURPRIJS")
        self.assertEqual(
            "HET WAS HET WITTE UUR NA HET MIDDAGMAAL, DE BLANKE PAGINA WAAROP HOOGUIT IETS MET POTLOOD WORDT GEKRIEBELD IN GEHEIMSCHRIFT, IETS OM ONMIDDELLIJK WEER UIT TE GUMMEN ZODRA DE ROLLUIKEN OMHOOG WORDEN GETROKKEN EN HET LEVEN OPNIEUW ZWART OP WIT EEN AANVANG NEEMT MET BONNETJES, BESTELLINGEN EN BEZWAARSCHRIFTEN",
            self.kws.permute_message(
                "ASO WLN ASO WUOOS QQM FL ASO DURRLEDLLC, RS ICLFJS HLEUFL WLLMGH AGGEQUO USON DSO HGOCGGR WGMRO ESJMUSISCR UF ESASUDNBAMUTO, USON GD GFDURRSCCUPJ WSSM QUO OS EQDDSF ZGRML RS MGCCQUJSF GDAGGE WGMRSF ESOMGJJSF SF ASO CSVSF GHFUSQW ZWLMO GH WUO SSF LLFVLFE FSSDO DSO IGFFSOPSN, ISNOSCCUFESF SF ISZWLLMNBAMUTOSF"))

    def test_2014_opgave_3c(self):
        self.kws.create_permutation_dict("HUGO BRANDT CORSTIUS")
        self.assertEqual("OOK BEKEND ONDER PSEUDONIEMEN PIET GRIJS, STOKER, RAOUL CHAPKIS EN BATTUS",
                         self.kws.permute_message(
                             "FFC UBCBEO FEOBL JMBQOFEDBIBE JDBP ALDTM, MPFCBL, LHFQS GNHJCDM BE UHPPQM"))

    def test_2015_opgave_3c(self):
        self.kws.create_permutation_dict("einstein")
        self.assertEqual("LOGICA BRENGT JE VAN A NAAR B. VERBEELDING BRENGT JE OVERAL",
                         self.kws.permute_message("HLBDNE IPTKBR FT VEK E KEEP I. VTPITTHSDKB IPTKBR FT LVTPEH"))

    def test_2016_opgave_3b(self):
        """
        Titels van nummers van David Bowie (1947-2016), vercijferd met een substitutie.
        Voor een uitleg van een substitutie met sleutel (codewoord)
        Sleutel is het personage dat zingt:
        """
        self.kws.create_permutation_dict("Aladdin Sane")
        self.assertEqual("TIME", self.kws.permute_message("TCJN"))
        self.kws.create_permutation_dict("Ziggy Stardust")
        self.assertEqual("ZIGGY STARDUST", self.kws.permute_message("XDAAW MNZLYOMN"))
        self.kws.create_permutation_dict("Halloween Jack")
        self.assertEqual("BIG BROTHER", self.kws.permute_message("ACN AQISJWQ"))
        self.kws.create_permutation_dict("Jareth the Goblin King")
        self.assertEqual("AS THE WORLD FALLS DOWN", self.kws.permute_message("JQ SOT WDPNE HJNNQ EDWC"))
        self.kws.create_permutation_dict("Major Tom")
        self.assertEqual("SPACE ODDITY", self.kws.permute_message("QLMJR KOODSY"))
        self.kws.create_permutation_dict("Hunky Dory")
        self.assertEqual("KOOKS", self.kws.permute_message("CIICP"))
        self.kws.create_permutation_dict("Thin White Duke")
        self.assertEqual("STATION TO STATION", self.kws.permute_message("PQTQKJG QJ PQTQKJG"))

    def test_2016_opgave_3c(self):
        self.kws.create_permutation_dict("UMBERTO ECO")
        self.assertEqual("DE NAAM VAN DE ROOS", self.kws.permute_message("ER IUUH VUI ER NJJP"))
        self.kws.create_permutation_dict("HARPER LEE")
        self.assertEqual("SPAAR DE SPOTVOGEL(S)", self.kws.permute_message("SNHHQ PE SNMTVMBEI(S)"))
        self.kws.create_permutation_dict("BENOÎTE GROULT")
        self.assertEqual("ZOUT OP MIJN HUID", self.kws.permute_message("ZHSQ HJ DULF RSUO"))
        self.kws.create_permutation_dict("EDWARD ALBEE")
        self.assertEqual("WIE IS ER BANG VOOR VIRGINIA WOOLF?",
                         self.kws.permute_message("VFR FQ RP DEKB UMMP UFPBFKFE VMMIL?"))
        self.kws.create_permutation_dict("MIEKE TELKAMP")
        self.assertEqual("WAARHEEN, WAARVOOR", self.kws.permute_message("WMMQPTTH, WMMQVJJQ"))
        self.kws.create_permutation_dict("TOOTS THIELEMANS")
        self.assertEqual("BLUESETTE", self.kws.permute_message("OCUIQIRRI"))

    # def test_20(self):
    #     self.kws.create_permutation_dict("")
    #     self.assertEqual("", self.kws.permute_message(""))
    #


class TestMorsecode(TestCase):
    def test_sos(self):
        self.assertEqual("SOS", morse_2_text(text_2_morse("sos")))

    def test_dna(self):
        self.assertEqual("DE SPITSMUIS", dna_2_text("ACCTCGCCCTCAACTCCTATCCCTAATCCATCCTCCC"))

    def test_morse_to_text(self):
        self.assertEqual("DESPITSMUIS", morse_2_text("-.. . ... .--. .. - ... -- ..- .. ..."))


class TestOTP(TestCase):
    def test_otp_decrypt(self):
        self.assertEqual("DETONGVANEENBLAUWEVINVISWEEGTTWEETON",
                         otp("YSHFWKGITXSSGWIEGIMBQZVTROIXLMLYDSSY", "VOORJELIGTOFFLIKKERTDENBVKERSTPUZZEL", -1))

        self.assertEqual("DETONGVANEENBLAUWEVINVISWEEGTTWEETON",
                         otp_decrypt("YSHFWKGITXSSGWIEGIMBQZVTROIXLMLYDSSY", "VOORJELIGTOFFLIKKERTDENBVKERSTPUZZEL"))

    def test_otp_encrypt(self):
        self.assertEqual("YSHFWKGITXSSGWIEGIMBQZVTROIXLMLYDSSY",
                         otp("DETONGVANEENBLAUWEVINVISWEEGTTWEETON", "VOORJELIGTOFFLIKKERTDENBVKERSTPUZZEL", 1))

        self.assertEqual("YSHFWKGITXSSGWIEGIMBQZVTROIXLMLYDSSY",
                         otp_encrypt("DETONGVANEENBLAUWEVINVISWEEGTTWEETON", "VOORJELIGTOFFLIKKERTDENBVKERSTPUZZEL"))


# class Vraag2018Negentien(TestCase):
#     def setUp(self):
#         self.kws = KeyWordSubstitution()
#
#     def test_2018_opgave_19_1(self):
#         self.kws.create_permutation_dict("hetro")
#         self.assertEqual("", self.kws.permute_message(
#             "􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃FMKCMTSFHGQPSKKMQVCVCMGMNHGNSINCHGNMOMDDSCEHDN􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))
#
#     def test_2018_opgave_19_2(self):
#         # self.kws.create_permutation_dict("hetro")
#         # self.assertEqual("", self.kws.permute_message(
#         #     "􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃QMORLQDITAPOFMQHCDAH􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))
#         self.assertEqual("", tabula_recta_decode(
#             "􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃QMORLQDITAPOFMQHCDAH􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬",
#             "marvel"))
#
#     def test_2018_opgave_19_3(self):
#         self.kws.create_permutation_dict("hetro")
#         self.assertEqual("", self.kws.permute_message(
#             "􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃CKSIOUPCIRKHHLPDNIGGLHRILD􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))
#
#     def test_2018_opgave_19_4(self):
#         self.kws.create_permutation_dict("hetro")
#         self.assertEqual("", self.kws.permute_message(
#             "􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃AZCZDFPJQCJNDCSCYDCQFPJNCD􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))
#
#     def test_2018_opgave_19_5(self):
#         self.kws.create_permutation_dict("hetro")
#         self.assertEqual("", self.kws.permute_message(
#             "􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃CDQIAJNEQGVAJNKNDWDDQN􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))


class TestCeasar(TestCase):

    def test_2011_opgave_7(self):
        """Ceasar encoded met de eerste letter van hun echte naam met A=0, B=1...
        Mercurius
        Venus
        Aarde
        Mars
        Jupiter
        Saturnus
        Uranus
        Neptunus"""
        self.assertEqual("YQDOGDUGE", caesar_cipher("Mercurius", 12).upper())
        self.assertEqual("QZIPN", caesar_cipher("Venus", 21).upper())
        self.assertEqual("AARDE", caesar_cipher("Aarde", 0).upper())  # Het antwoord omdat deze miste
        self.assertEqual("YMDE", caesar_cipher("Mars", 12).upper())
        self.assertEqual("SDYRCNA", caesar_cipher("Jupiter", 9).upper())
        self.assertEqual("KSLMJFMK", caesar_cipher("Saturnus", 18).upper())
        self.assertEqual("OLUHOM", caesar_cipher("Uranus", 20).upper())
        self.assertEqual("ARCGHAHF", caesar_cipher("Neptunus", 13).upper())

    def test_2011_opgave_12(self):
        # [print(caesar_cipher("gezelligheid", x)) for x in range(26)]
        # for i, item in enumerate(list("abcddeafbeg")):
        #     print(i, caesar_cipher(item, i + 6))
        self.assertEqual("gezelligheid", caesar_cipher("aytyffcabycx", 6))

    def test_2014_opgave_6b(self):
        self.assertEqual("CAESAR", caesar_cipher("FDHVDU", -3).upper())


class TestVingenere(TestCase):
    def test_2014_opgave_6c(self):
        self.assertEqual("QQAMIAIII", tabula_recta("VINGENERE", "vingenere"))
        self.assertEqual("VINGENERE", tabula_recta_decode("QQAMIAIII", "vingenere"))


class TestNumberSubstitution(TestCase):
    def test_number_to_text(self):
        self.assertEqual("DE GEDAAGDE BAGAGEDIEF GAF DE BEEDIGDE CHEF DE ACACIA",
                         numbers_to_text("45075411745021717549560716045025549745038560450131391"))

    def test_text_to_numbers(self):
        self.assertEqual("45075411745021717549560716045025549745038560450131391",
                         text_to_numbers("DE GEDAAGDE BAGAGEDIEF GAF DE BEEDIGDE CHEF DE ACACIA"))

    def test_text_to_numbers_by_keyword(self):
        self.assertEqual("29120192752306278295032782921123209262940327829",
                         text_to_numbers_by_keyword("ELKE KLEUTER PEUZELT REUZELEKKERE LEPELS REUZEL", "kerstpuzzel"))

    def test_numbers_to_text_by_keyword(self):
        self.assertEqual("ELKE KLEUTER PEUZELT REUZELEKKERE LEPELS REUZEL",
                         numbers_to_text_by_keyword("29120192752306278295032782921123209262940327829", "kerstpuzzel"))


class BifidUnitTests(unittest.TestCase):
    def test_unique_key(self):
        self.assertEqual("LETRONWPSABCDFGHIKMQUVXYZ", bifid_key("LETTERONTWERPERS"))
        self.assertEqual("LETRONWPSIABCDFGHKMQUVXYZ", bifid_key("LETTERONTWERPERSJ"))
        self.assertEqual("IABCDEFGHKLMNOPQRSTUVWXYZ", bifid_key("IJ"))

    def test_pos(self):
        self.assertEqual((3, 5), pos("LETRONWPSABCDFGHIKMQUVXYZ", "G"))

    def test_en_decript(self):
        self.assertEqual("ANNEMARIEIORRITSMA",
                         bifid_decrypt("Politicus", bifid_encrypt("Politicus", "Annemarie Jorritsma")))


class MonoAlfabeticSubstitution(unittest.TestCase):

    def setUp(self):
        self.kws = KeyWordSubstitution()

    def test_2011_opgave_8(self):
        self.kws.create_permutation_dict("LINEAIRE ALGEBRA")
        self.assertEqual("""DECOD EBEST AATUI TVIJF GETAL LENHE TVIJF DEPLU
        SHETD ERDEG ETALI SGELI JKAAN VIJFT IENHE TVIER
        DEGET ALISD RIEME ERDAN HETTW EEDEH ETEER STEGE
        TALIS TWEEM INDER DANVI JFKEE RHETT WEEDE GETAL
        HETTW EEDEP LUSHE TDERD EGETA LISGE LIJKA ANTIE
        NDESO MVANA LLEGE TALLE NISGE LIJKA ANDER TIG""", encryptMessage(self.kws.get_permutation_alphabet(), """JDIPJ DHDST EETUB TVBMK GDTEA ADCLD TVBMK JDQAU
        SLDTJ DFJDG DTEAB SGDAB MNEEC VBMKT BDCLD TVBDF
        JDGDT EABSJ FBDOD DFJEC LDTTW DDJDL DTDDF STDGD
        TEABS TWDDO BCJDF JECVB MKNDD FLDTT WDDJD GDTEA
        LDTTW DDJDQ AUSLD TJDFJ DGDTE ABSGD ABMNE ECTBD
        CJDSP OVECE AADGD TEAAD CBSGD ABMNE ECJDF TBG"""))


class SmsTest(TestCase):

    def setUp(self) -> None:
        self.sms = Sms()

    def test_word_2_sms(self):
        self.assertEqual("42556", self.sms.word_2_sms("Hallo"))

    def test_sms_2_word(self):
        self.assertEqual(['WERELDBURGER'], self.sms.sms_2_word(self.sms.word_2_sms("wereldburger")))


if __name__ == '__main__':
    unittest.main()
