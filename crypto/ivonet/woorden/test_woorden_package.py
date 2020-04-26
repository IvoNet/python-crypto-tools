import re
from unittest import TestCase, main

from ivonet.woorden.DictionaryRegexer import DictionaryRegexer
from ivonet.woorden.analyse_sentence import StringWordAnalyser
from ivonet.woorden.woordenboek import Woordenboek


class TestWoordenboek(TestCase):
    def setUp(self):
        self.wb = Woordenboek()

    def test_is_woord(self):
        self.assertTrue(self.wb.is_word("regen"))
        self.assertTrue(self.wb.is_word("aalsmeerder"))

    def test_anagram(self):
        self.assertEqual(['SERVISCH', 'VISSCHER'], self.wb.anagram("servisch"))
        self.assertEqual(['SERVISCH', 'VISSCHER'], self.wb.anagram("servisch"))
        anagram = self.wb.anagram("SHOTSCOLA")  # rits SCHOTS en COLA naar SCHOOLTAS of zoek het gewoon op :-)
        anagram.sort()
        self.assertListEqual(['SCHOOLTAS', 'SHOTSCOLA'], anagram)

    def test_ends_with(self):
        self.assertEqual(['DOCTOR', 'EREDOCTOR', 'SPINDOCTOR'], self.wb.ends_with("DOCTOR"))

    def test_starts_with(self):
        self.assertEqual(
            ['HETER', 'CATHETER', 'KATHETER', 'BALLONKATHETER', 'BLAASKATHETER', 'URINEKATHETER', 'MAAGKATHETER'],
            self.wb.ends_with("HETER"))

    def test_contains(self):
        self.assertEqual(
            ['LIEFDE', 'BLIEFDE', 'KLIEFDE', 'LIEFDEN', 'LIEFDES', 'BELIEFDE', 'BLIEFDEN', 'GELIEFDE', 'KLIEFDEN',
             'VERLIEFDE', 'APENLIEFDE', 'BOEKENLIEFDE', 'BROEDERLIEFDE', 'CLUBLIEFDE', 'DIERENLIEFDE', 'EIGENLIEFDE',
             'EX-GELIEFDE', 'FILMLIEFDE', 'GESLACHTSLIEFDE', 'HAAT-LIEFDEVERHOUDING', 'HERENLIEFDE', 'JEUGDLIEFDE',
             'JONGENSLIEFDE', 'KALVERLIEFDE', 'KINDERLIEFDE', 'KNAPENLIEFDE', 'LIEFDEBAND', 'LIEFDEBETREKKING',
             'LIEFDEBETUIGING', 'LIEFDEBEURT', 'LIEFDEBLIJK', 'LIEFDEBRIEF', 'LIEFDEDAAD', 'LIEFDEDIENST', 'LIEFDEGAVE',
             'LIEFDEGEBOD', 'LIEFDEGESCHIEDENIS', 'LIEFDEGESTICHT', 'LIEFDEGIFT', 'LIEFDEGROET', 'LIEFDEKRACHT',
             'LIEFDELEVEN', 'LIEFDELOOS', 'LIEFDELOOSHEID', 'LIEFDEMAAL', 'LIEFDERIJK', 'LIEFDESAFFAIRE',
             'LIEFDESAVONTUUR', 'LIEFDESBABY', 'LIEFDESBAND', 'LIEFDESBELEVING', 'LIEFDESBETREKKING',
             'LIEFDESBETUIGING', 'LIEFDESBOODSCHAP', 'LIEFDESBRIEF', 'LIEFDESDAAD', 'LIEFDESDRAMA', 'LIEFDESDRANK',
             'LIEFDESENERGIE', 'LIEFDESFILM', 'LIEFDESGEBIED', 'LIEFDESGEDICHT', 'LIEFDESGELUK', 'LIEFDESGESCHIEDENIS',
             'LIEFDESGOD', 'LIEFDESGODIN', 'LIEFDESIDEAAL', 'LIEFDESKIND', 'LIEFDESKOPPEL', 'LIEFDESKRACHT',
             'LIEFDESLEED', 'LIEFDESLEVEN', 'LIEFDESLIED', 'LIEFDESLYRIEK', 'LIEFDESMART', 'LIEFDESNAAM',
             'LIEFDESNACHT', 'LIEFDESNEST', 'LIEFDESNESTJE', 'LIEFDESOBJECT', 'LIEFDESPAAR', 'LIEFDESPAD',
             'LIEFDESPARTNER', 'LIEFDESPEL', 'LIEFDESPIJN', 'LIEFDESPOEZIE', 'LIEFDESRELATIE', 'LIEFDESROMAN',
             'LIEFDESSCENE', 'LIEFDESSPEL', 'LIEFDESTHEMA', 'LIEFDESVERDRIET', 'LIEFDESVERHAAL', 'LIEFDESVERHOUDING',
             'LIEFDESVERKLARING', 'LIEFDESVERLANGEN', 'LIEFDESVERRAAD', 'LIEFDESVUUR', 'LIEFDEVERKLARING', 'LIEFDEVOL',
             'LIEFDEWERK', 'LIEFDEZUSTER', 'MANNENLIEFDE', 'MENSENLIEFDE', 'MOEDERLIEFDE', 'NAASTENLIEFDE',
             'NATUURLIEFDE', 'OUDERLIEFDE', 'VADERLANDSLIEFDE', 'VADERLIEFDE', 'VAKANTIELIEFDE', 'VOORLIEFDE',
             'VRIJHEIDSLIEFDE', 'VROUWENLIEFDE', 'WAARHEIDSLIEFDE', 'WEDERLIEFDE', 'ZOMERLIEFDE', 'ZUSTERLIEFDE',
             'LIEFDESERVARING', 'LIEFDESSMART', 'HAAT-LIEFDERELATIE', 'KONINGSLIEFDE', 'BELIEFDEN', 'DOORKLIEFDE',
             'DOORKLIEFDEN', 'GEKLIEFDE', 'GEKLIEFDEN', 'GELIEFDEN', 'GELIEFDER', 'GELIEFDERE', 'KALVERLIEFDES',
             'LIEFDEBANDEN', 'LIEFDEBETUIGINGEN', 'LIEFDEBEURTEN', 'LIEFDEBLIJKEN', 'LIEFDEBRIEVEN', 'LIEFDEDIENSTEN',
             'LIEFDEGAVEN', 'LIEFDEGESTICHTEN', 'LIEFDEGIFTEN', 'LIEFDELOZE', 'LIEFDELOZER', 'LIEFDEMALEN',
             'LIEFDERIJKE', 'LIEFDERIJKER', 'LIEFDERIJKSTE', 'LIEFDESAVONTUREN', 'LIEFDESBETREKKINGEN',
             'LIEFDESBETUIGINGEN', 'LIEFDESBRIEVEN', "LIEFDESDRAMA'S", 'LIEFDESFILMS', 'LIEFDESGESCHIEDENISSEN',
             'LIEFDESLIEDJE', 'LIEFDESLIEDJES', 'LIEFDESPAARTJE', 'LIEFDESRELATIES', 'LIEFDESROMANS', 'LIEFDESVERHALEN',
             'LIEFDESVERKLARINGEN', 'LIEFDESVERSJE', 'LIEFDEVERKLARINGEN', 'LIEFDEVOLLE', 'LIEFDEWERKEN',
             'LIEFDEZUSTERS', 'SMOORVERLIEFDE', 'TEERGELIEFDE', 'VEELGELIEFDE', 'VERLIEFDEN', 'VERLIEFDER',
             'VOORLIEFDES', 'WELGELIEFDE', 'ZIELSGELIEFDE', 'JEUGDLIEFDES', 'LIEFDEBETREKKINGEN', 'LIEFDEDADEN',
             'LIEFDEGESCHIEDENISSEN', 'LIEFDESAFFAIRES', 'LIEFDESGEDICHTEN', 'LIEFDESLIEDEREN', 'LIEFDESPAREN',
             'LIEFDESPARTNERS', 'LIEFDESSCENES', 'LIEFDEVOLLER', 'LIEFDEVOLLERE', 'STAPELVERLIEFDE', 'LIEFDESDRANKEN',
             'LIEFDESVERHOUDINGEN', 'LIEFDELOOST', 'ONGELIEFDE', 'BALVERLIEFDE', 'LIEFDESAVONTUURTJE',
             'LIEFDESROMANNETJE', 'LIEFDESERVARINGEN', 'LIEFDESDADEN', 'HAAT-LIEFDEVERHOUDINGEN', 'LIEFDESNACHTEN',
             'LIEFDESDRANKJES', 'VAKANTIELIEFDES', 'LIEFDESVERHAALTJE', 'LIEFDESBANDEN', 'LIEFDESLEVENS',
             'LIEFDESDRANKJE', 'LIEFDESGEDICHTJE', 'LIEFDESBRIEFJES', 'LIEFDESGEDICHTJES', 'LIEFDESROMANNETJES',
             'LIEFDESVERHAALTJES', 'LIEFDESVERLANGENS', 'LIEFDESAVONTUURTJES', 'LIEFDEKRACHTEN', 'LIEFDESPIJNEN',
             'LIEFDESKOPPELTJE', "LIEFDESBABY'S", 'LIEFDESSPELLETJES', 'LIEFDESBRIEFJE', 'LIEFDESNESTJES',
             'LIEFDESBOODSCHAPPEN', 'HAATLIEFDE', 'LIEFDEBLIKKEN', 'LIEFDEGEDICHTEN', 'LIEFDELIED', 'LIEFDERIJKEN',
             'HAATLIEFDEVERHOUDING', 'HAATLIEFDE-VERHOUDING'],
            self.wb.contains("liefde"))

    def test_not_contains(self):
        self.assertEqual(['AU',
                          'HA',
                          'HUH',
                          'QUA',
                          'A',
                          'A3',
                          'A4',
                          'AAA',
                          'AA',
                          'HAU',
                          'HU',
                          'AH',
                          'AHA',
                          'H',
                          'HAHA',
                          'Q',
                          'Q.Q.',
                          'U',
                          '06'], self.wb.not_contains("BCDEFGIJKLMNOPRSTVWXYZ"))

    def test_by_same_word_plus_one_letter(self):
        self.assertEqual(['BOOMKLEVER'], self.wb.by_same_word_plus_one_letter("BOOMKEVER"))
        self.assertSequenceEqual(['KREKEL', 'REKELS'], self.wb.by_same_word_plus_one_letter("rekel"))


class DictionaryRegexerTestCase(TestCase):
    def setUp(self):
        self.regexer = DictionaryRegexer()

    def test_pattern_to_regex(self):
        self.assertEqual('abc...ghi', self.regexer.pattern_to_regexp('abc...ghi'))
        self.assertEqual('abc[\w]*ghi', self.regexer.pattern_to_regexp('abc*ghi'))

    def test_regex(self):
        self.assertEqual(['ABC', 'abc'], re.findall('abc', 'ABC\nabc', re.IGNORECASE))


class StringWordAnalyserTest(TestCase):
    def test_valid(self):
        a = StringWordAnalyser()
        self.assertTrue(a.all_words("eN"))
        self.assertTrue(a.all_words("EENWERELDVAN"))
        self.assertTrue(a.all_words("ALLEMAALHAATENHALLOWERELDWIJZIJNMENSENMETHETGROTEGELUK"))

    def test_invalid(self):
        a = StringWordAnalyser()
        self.assertFalse(a.all_words("ACHTWANARAMVNRATECCTIRASNENSUVOLLAITEEAS"))
        self.assertFalse(a.all_words("ACHTWANARAMVNRATECCTIRASNENSUVOLLWERELD"))
        self.assertFalse(a.all_words("nn"))


if __name__ == '__main__':
    main()
