#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import os
import pickle

from ivonet.string import remove_accents


def read_txt_file_current_path_no_diacritics(fi):
    with open(get_txt_file(fi), "r", encoding='latin1') as fl:
        return remove_accents(fl.read())


def txt_file_upper_lines(fi):
    return read_txt_file_current_path_no_diacritics(fi).strip().upper().split("\n")


def un_pickle(fi):
    if os.path.exists(get_pickle_file(fi)):
        with open(get_pickle_file(fi), "rb") as fl:
            return pickle.load(fl)
    return {}


def in_pickle(fo, values):
    with open(get_pickle_file(fo), 'wb') as fl:
        pickle.dump(values, fl)


def get_src_dir():
    src_dir = os.path.join(os.path.dirname(__file__), '..')
    _ensure_dir_exists(src_dir)
    return src_dir


def get_source_dir(extension):
    folder = os.path.join(get_src_dir(), extension)
    _ensure_dir_exists(folder)
    return folder


def get_config_dir():
    return get_source_dir('files/config')


def get_img_dir():
    return get_source_dir('files/img')


def get_pickle_dir():
    return get_source_dir('files/pickles')


def get_txt_dir():
    return get_source_dir('files/txt')


def get_csv_dir():
    return get_source_dir('files/csv')


def get_profile_dir():
    return get_source_dir('files/profile')


def get_txt_file(fi):
    return os.path.join(get_txt_dir(), fi)


def get_csv_file(fi):
    return os.path.join(get_csv_dir(), fi)


def get_pickle_file(fi):
    return os.path.join(get_pickle_dir(), fi)


def _ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.mkdir(directory, mode=0o777)


def clean_csv_file(file_name_in, file_name_out):
    patterns = dict()
    #     patterns['\"\"'] = '\"'
    patterns['\\\"'] = ''
    with open(file_name_in, 'r') as f:
        lines = f.readlines()
        with open(file_name_out, 'w') as g:
            for line in lines:
                for pattern, subs in patterns.items():
                    if pattern in line:
                        line = line.replace(pattern, subs)
                g.write(line)


def cat(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)


def grep(pattern, file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if pattern in line:
                print(line)


def head(lines, file_name):
    i_line = 0
    with open(file_name, 'r') as f:
        while i_line < lines:
            line = f.readline()
            print(line)
            i_line += 1
