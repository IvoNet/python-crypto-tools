#!/usr/bin/env python3

letter_dic = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20,
              "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31,
              "W": 32, "X": 33, "Y": 34, "Z": 35,
              "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

letters = {ord(k): str(v) for k, v in letter_dic.items()}


def chech_validation_chars_iban(iban):
    zeros_iban = iban[:2] + '00' + iban[4:]
    iban_inverted = zeros_iban[4:] + zeros_iban[:4]
    iban_numbered = iban_inverted.translate(letters)

    verification_chars = 98 - (int(iban_numbered) % 97)

    if verification_chars < 10:
        verification_chars = '{:02}'.format(int(verification_chars))
    return verification_chars


def validate_iban(iban):
    iban_inverted = iban[4:] + iban[:4]
    iban_numbered = iban_inverted.translate(letters)

    return int(iban_numbered) % 97


if __name__ == '__main__':
    my_iban = 'NL62RABO0134637267'

    if chech_validation_chars_iban(my_iban) == int(my_iban[2:4]):
        if validate_iban(my_iban) == 1:
            print('IBAN ok!\n')
        else:
            print('IBAN nok!\n')
    else:
        print('IBAN nok!\n')
