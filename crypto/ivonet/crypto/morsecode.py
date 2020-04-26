#!/usr/bin/envpython
# -*-coding:utf-8-*-
from ivonet.collection.dictinary import reverse_dict
from ivonet.log import _

__doc__ = """
Morse module
"""

morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    ":": "---...",
    "'": ".----.",
    ")": "-.--.-",
    ";": "-.-.-",
    "(": "-.--.",
    "=": "-...-",
    "@": ".--.-.",
    "&": ".–..."}

alphabet_morse = reverse_dict(morse_alphabet)
_(alphabet_morse)


def text_2_morse(txt, delimiter=" ") -> str:
    """
# Text 2 Morse code

This function will translate standard text to morse code.
    """
    answer = ""
    for x in txt.upper():
        answer += morse_alphabet[x]
        answer += delimiter
    return answer


def morse_2_text(morse, delimiter=" ") -> str:
    """
# Morse code 2 Text

This function will translate Morse code to standard text. Please note that every morse 'letter' should be
separated by the delimiter (= space).
    """
    answer = ""
    for x in morse.strip().split(delimiter):
        answer += alphabet_morse[x]
    return answer


def __letters_as_morse_2_text(dna, short="C", long="A", letter_delimiter="T", word_delimiter="G"):
    """Creates a morse sequence from dna letters (ACTG) to be decided is that
    are delimiters for words and letters"""
    morse = dna.replace(short, ".").replace(long, "-")
    morse_words = morse.split(word_delimiter)
    sentence = ""
    for morse_word in morse_words:
        morse_letters = morse_word.split(letter_delimiter)
        word = ""
        for morse_letter in morse_letters:
            word += morse_2_text(morse_letter)
        sentence += word + " "
    return sentence.strip()


def dna_2_text(payload, short="C", long="A", letter_delimiter="T", word_delimiter="G"):
    """Legacy code. just for keeping the name as I used it in 2017 for the dna question"""
    return letters_as_morse_2_text(payload, short=short, long=long, letter_delimiter=letter_delimiter,
                                   word_delimiter=word_delimiter)


def letters_as_morse_2_text(payload, short="A", long="B", letter_delimiter="C", word_delimiter="D"):
    """
    Translates letters as morse replacements.

    :param payload: the letters representing the morse code
    :param short: the letter representing the morse 'short'
    :param long: the letter representing the morse 'long'
    :param letter_delimiter: the letter representing the end of a letter
    :param word_delimiter: the letter representing the end of a word
    :return: translated text or None if no translation could be had.
    """
    try:
        return __letters_as_morse_2_text(payload, short=short, long=long, letter_delimiter=letter_delimiter,
                                         word_delimiter=word_delimiter)
    except KeyError:
        return None


if __name__ == '__main__':
    # CODE = "ACACAT"
    # print(letters_as_morse_2_text(CODE, short="A", long="C", letter_delimiter="T", word_delimiter="G"))
    # print(letters_as_morse_2_text(CODE, short="C", long="A", letter_delimiter="T", word_delimiter="G"))
    # print(letters_as_morse_2_text(CODE, short="A", long="T", letter_delimiter="C", word_delimiter="G"))
    print(morse_2_text("-.. . ... .--. .. - ... -- ..- .. ..."))  # A = - C = . -> DE SPITSMUIS
    print(morse_2_text(
        "..-. . . .-.. .. -. --. .. --. .- .-- .... . -. .. .-.. --- --- -.- - --- - .... . .-- . ... - .- -. -.. -- -.-- ... .--. .. .-. .. - .. ... -.-. .-. -.-- .. -. --. ..-. --- .-. .-.. . .- ...- .. -. --."))  # A = - C = .
    print(morse_2_text(""))  # R = . G = - B = delim
