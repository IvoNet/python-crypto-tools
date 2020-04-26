#!/usr/bin/env python
#  -*- coding: utf-8 -*-
# Simple Substitution Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import random
import sys

from ivonet.crypto.key_word_substitution import KeyWordSubstitution

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    kws = KeyWordSubstitution()
    kws.create_permutation_dict("LINEIAREALGEBRA")
    myMessage = """
JDIPJ DHDST EETUB TVBMK GDTEA ADCLD TVBMK JDQAU
SLDTJ DFJDG DTEAB SGDAB MNEEC VBMKT BDCLD TVBDF
JDGDT EABSJ FBDOD DFJEC LDTTW DDJDL DTDDF STDGD
TEABS TWDDO BCJDF JECVB MKNDD FLDTT WDDJD GDTEA
LDTTW DDJDQ AUSLD TJDFJ DGDTE ABSGD ABMNE ECTBD
CJDSP OVECE AADGD TEAAD CBSGD ABMNE ECJDF TBG    
    """
    myKey = kws.get_permutation_alphabet()  # gotten from key_word_substitution
    # myMessage = 'When you do the common things in life in an uncommon way, you will command the attention of the world'
    # myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    myMode = 'encrypt'  # set to 'encrypt' or 'decrypt'

    checkValidKey(myKey)

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated


def get_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
    # cipher = decrypt("PRUPQDQRQDI", "substitutie")
    # print(cipher)
