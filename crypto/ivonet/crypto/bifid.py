#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from ivonet.log import _
from ivonet.string.alphabet import alphabet


# https://nl.wikipedia.org/wiki/Bifidcijfer

def bifid_key(letters):
    AB = letters.upper().replace("J", "I").replace(" ", "") + alphabet(True).replace("J", "")
    _(AB)
    ret = ""
    for l in AB:
        if l in ret:
            continue
        ret += l
    _(ret)
    return ret


def pos(key, letter):
    position = key.find(letter.upper())
    row = (position // 5) + 1
    col = (position % 5) + 1
    return row, col


def letter(key, pos):
    x, y = pos
    x -= 1
    y -= 1
    p = x * 5 + y
    return key[p]


def bifid_encrypt(key, text):
    """
# BIFID Encrypt

This method encrypts the provided text with the provided key according to the BIFID algorithm

Read more about it [here](https://nl.wikipedia.org/wiki/Bifidcijfer)
    """
    txt = text.upper().replace(" ", "").replace("J", "I")
    bkey = bifid_key(key)
    ret = [pos(bkey, x) for x in txt]
    x, y = list(zip(*ret))
    ret = list(x)
    ret.extend(y)
    answer = ""
    for i in range(0, len(ret), 2):
        answer += letter(bkey, (ret[i], ret[i + 1],))
    return answer


def bifid_decrypt(key, text):
    """
# BIFID Decrypt

This method decrypts the provided text with the provided key according to the BIFID algorithm

Read more about it [here](https://nl.wikipedia.org/wiki/Bifidcijfer)
    """
    txt = text.upper().replace(" ", "")
    bkey = bifid_key(key)
    ret = [pos(bkey, x) for x in txt]
    numbers = ""
    for row, col in ret:
        numbers = numbers + str(row) + str(col)
    row = list(numbers[0:int(len(numbers) / 2)])
    col = list(numbers[int(len(numbers) / 2):])
    ret = list(zip(row, col))
    return ''.join([letter(bkey, (int(r), int(c))) for r, c in ret])


if __name__ == '__main__':
    print(bifid_key("vijftigers"))
    print(bifid_encrypt("letterontwerpers", "gerard unger"))
    print(bifid_decrypt("letterontwerpers", "BETVBOSYBOS"))
