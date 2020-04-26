#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""One-time pad encrypter and decrypter.

These methods can encrypt printable text message using the specified key.

See also here: http://rumkin.com/tools/cipher/otp.html
"""
from ivonet.string.alphabet import alphabet


def otp(text, key_txt, encdec=-1):
    """encdec = -1 for decode, 1 for encode
    text = the text to encode or decode.
    key = the key (pad) to use"""
    pad = ""
    out = ""
    c = ""
    key = key_txt.upper()
    for x in key:
        if x in alphabet(upper=True):
            pad += x

    for x in text:
        uc = " "
        if x in alphabet(upper=True):
            uc = "A"
        if x in alphabet():
            uc = "a"
        if uc != " ":
            if len(pad) == 0:
                pad = "AAAAAAAA"
            c = ord(x) - ord(uc[0]) + encdec * (ord(pad[0]) - ord("A"))
            c = (c + 26) % 26
            c = chr(ord(uc[0]) + c)
            pad = pad[1: len(pad)]
        out += c
    return out


def otp_decrypt(text, key):
    return otp(text, key, encdec=-1)


def otp_encrypt(text, key):
    return otp(text, key, encdec=1)


if __name__ == '__main__':
    print(otp("YSHFWKGITXSSGWIEGIMBQZVTROIXLMLYDSSY", "VOORJELIGTOFFLIKKERTDENBVKERSTPUZZEL", -1))
    print("YSHFWKGITXSSGWIEGIMBQZVTROIXLMLYDSSY" == otp("DETONGVANEENBLAUWEVINVISWEEGTTWEETON",
                                                        "VOORJELIGTOFFLIKKERTDENBVKERSTPUZZEL", 1))
