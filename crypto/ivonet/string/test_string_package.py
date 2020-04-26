#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from unittest import TestCase, main

from ivonet.string import substring_after_character, alphabet
from ivonet.string.alphabet import base_26_encode_string, sum_letter_values_of_word, product_letter_values_of_word, \
    alphabet
from ivonet.string.string_functions import sort_alphabetical, is_sorted, letters, letters_is_word, word_frequency_counter


class TestSubstringAfterCharacter(TestCase):
    def test_gw_01(self):
        line = 'before_20141017'
        character = '_'
        r = substring_after_character(line, character)
        e = '20141017'
        self.assertEqual(r, e, 'line')

    def test_gw_02(self):
        line = 'before_20141017'
        character = '_'
        r = substring_after_character(line, character,
                                      include_character=True)
        e = '_20141017'
        self.assertEqual(r, e, 'line')

    def test_gw_03(self):
        line = 'before_20141017'
        character = '_'
        r = substring_after_character(line, character,
                                      include_character=False)
        e = '20141017'
        self.assertEqual(r, e, 'line')

    def test_gw_04(self):
        line = 'before_20141017'
        character = '.'
        r = substring_after_character(line, character,
                                      include_character=True)
        self.assertIs(r, None, 'If character not in line, None shall be returned.')


class TestAlphabet(TestCase):
    def test_base_26_encoded(self):
        self.assertEqual(0, base_26_encode_string("A"))
        self.assertEqual(1, base_26_encode_string("B"))
        self.assertEqual(25, base_26_encode_string("z"))
        self.assertEqual(26, base_26_encode_string("ba"))
        self.assertEqual(16197, base_26_encode_string("XYZ"))
        self.assertEqual(3296799508237, base_26_encode_string("PUMEGENMB"))
        self.assertEqual(9849791328331451697274678861440325, base_26_encode_string(alphabet()))
        self.assertEqual(
            20569858802338608448364049446852061780140090404415032130205785332253615286792604334631099850853638206681253072973938092469074262459481025482721597642516904700401181296799991465053389302729514,
            base_26_encode_string(
                "FCJNIPMLEEUHUATKMSOZUTXLEZBBFTLKYHXLLORKXQDDIFJCDCZGJWANKVALRMVNZSDRRHDXEICQVBSLUKKLYVEWGGFOKUHEBPHIHLIJPXTQEOANYBDOIWPLKRLVNXTKVGBCDSK"))

    def test_sum_letter_values_of_word(self):
        self.assertEqual(3, sum_letter_values_of_word("aaa"))
        self.assertEqual(27, sum_letter_values_of_word("az"))
        self.assertEqual(25, sum_letter_values_of_word("az", 0))
        self.assertEqual(351, sum_letter_values_of_word(alphabet()))

    def test_product_letter_values_of_word(self):
        self.assertEqual(403291461126605635584000000, product_letter_values_of_word(alphabet()))


class StringFunctions(TestCase):
    def test_sort_alphanumerical(self):
        self.assertEqual("abdij", sort_alphabetical("abdij"))
        self.assertEqual("jidba", sort_alphabetical("abdij", True))

    def test_is_sorted(self):
        self.assertFalse(is_sorted("za"))
        self.assertTrue(is_sorted("za", True))
        self.assertTrue(is_sorted("aabbccdd"))

    def test_letters(self):
        self.assertEqual("HW", letters("Hallo Wereld"))
        self.assertEqual("ae", letters("Hallo Wereld", 1))

    def test_letters_is_word(self):
        self.assertFalse(letters_is_word("Hallo Wereld"))  # HW
        self.assertTrue(letters_is_word("Hallo en gedag"))  # Heg
        self.assertTrue(letters_is_word("Hallo wereld burger leger waar", 3))  # leger

    def test_word_frequency(self):
        self.assertEqual(29, word_frequency_counter(['noll', 'hu', 'tonde', 'tonko', 'noll', 'tonko', 'tonde', 'tongo', 'de', 'de', 'go', 'tonde', 'tonko', 'me', 'la', 'tonko', 'ra', 'go', 'tonti', 'tonko', 'hu', 'go', 'tonsu', 'go', 'la', 'tonko', 'me', 'tonde', 'tonhu', 'tonko', 'ti', 'noll', 'la', 'tonko', 'tonde', 'tonti', 'noll', 'noll', 'tonti', 'tonko', 'noll', 'tonko', 'by', 'go', 'hu', 'me', 'ni', 'ko', 'tonko', 'noll', 'noll', 'la', 'tonko', 'tonra', 'tonko', 'fy', 'hu', 'tongo', 'tonde', 'tonko', 'tonme', 'tonko', 'fy', 'hu', 'tongo', 'tonde', 'tonko', 'tonni', 'tonvy', 'tonko', 'tonby', 'go', 'tonan', 'ko', 'tonko', 'me', 'tonde', 'tonko', 'tonra', 'tonhu', 'tonko', 'tonme', 'tonko', 'me', 'tonde', 'tonko', 'tonde', 'fy', 'go', 'hu', 'tonko', 'go', 'la', 'tonko', 'tonni', 'tonko', 'me', 'tonde', 'tonko', 'ni', 'go', 'tonko', 'vy', 'po', 'la', 'ti', 'tonko', 'ti', 'me', 'de', 'ra', 'tonti', 'tonko', 'ra', 'po', 'tongo', 'ti', 'go', 'la', 'tonvy']).frequency("tonko"))


if __name__ == "__main__":
    main()
