#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from ivonet.file import get_csv_file
from ivonet.string.string_functions import initialize

TOP2000 = [x.split(";") for x in
           (open(get_csv_file("TOP-2000-2018.csv"), "r", encoding='latin1').read().split("\n"))]


# print(TOP2000)


def from_artist(artist):
    return [x for x in TOP2000 if x[2] == artist]


def all_titles():
    return [x[1] for x in TOP2000]


def all_artists():
    return [x[2] for x in TOP2000]


def set_artists():
    return set(all_artists())


def titles_with_x_words(value):
    return [x[1] for x in TOP2000 if len(x[1].split(" ")) is value]


def get(rank):
    return [x for x in TOP2000 if x[0] == str(rank)][0]


def year(rank):
    pass


def all_first_letters_of_titles():
    letters = []
    ret = [x[1].split() for x in TOP2000]
    for title in ret:
        let = []
        for word in title:
            let.append(word[0])
        letters.append("".join(let))
    return letters


def by_title_first_letters(payload):
    to_find = payload.upper()
    ret = []
    for item in TOP2000:
        if to_find == initialize(item[1]):
            ret.append(item)
    return ret


if __name__ == '__main__':
    # print(from_artist("Queen"))
    # print(all_first_letters_of_titles())
    # print(all_artists())
    # print(all_titles())
    print(get(input("Number: ")))
