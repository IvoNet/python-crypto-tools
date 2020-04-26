dutch_values = [1, 3, 3, 1, 1, 5, 2, 2, 1, 4, 4, 2, 3, 1, 1, 3, 10, 1, 1, 1, 4, 4, 4, 8, 8, 6]


def getValue(c):
    return dutch_values[ord(c) - ord('a')]


def scrabble(word):
    x = 0
    for l in word:
        x += getValue(l)
    return x


def scrabble_numbers_4_letters(word):
    return "".join([str(getValue(x)) for x in word])


if __name__ == '__main__':
    print(scrabble("ivo"))
    print(scrabble_numbers_4_letters("ivo"))
