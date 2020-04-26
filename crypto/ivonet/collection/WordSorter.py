import string


class WordSorter(object):

    def __init__(self, words=[]):
        self.w = list(words)

    def sort_words(self, method_to_call):
        kpi_list = list()
        kpi_dict = dict()
        method_to_call = getattr(self, method_to_call)
        for w in self.w:
            kpi = method_to_call(w)
            kpi_list.append(kpi)
            kpi_dict[w] = kpi
        words_sorted = [i[0] for i in sorted(zip(self.w, kpi_list),
                                             key=lambda l: l[1], reverse=True)]

        for w in words_sorted:
            print('{}\t{}'.format(kpi_dict[w], w))

    @staticmethod
    def nr_letters(word):
        return len(word)

    @staticmethod
    def nr_vowels(word):
        w = ''.join([x for x in word if x in ['A', 'E', 'I', 'O', 'U']])
        return len(w)

    @staticmethod
    def nr_first_half(word):
        first_half = string.ascii_uppercase[0:13]
        w = ''.join([x for x in word if x in first_half])
        return len(w)

    @staticmethod
    def nr_last_half(word):
        first_half = string.ascii_uppercase[13:26]
        w = ''.join([x for x in word if x in first_half])
        return len(w)

    @staticmethod
    def position_up_to_alphabetical(word):
        for i in range(1, len(word)):
            if ord(word[i]) < ord(word[i - 1]):
                return i
        return len(word)

    @staticmethod
    def nr_even_letters(word):
        even_letters = string.ascii_uppercase[0::2]
        w = ''.join([x for x in word if x in even_letters])
        return len(w)

    @staticmethod
    def nr_odd_letters(word):
        odd_letters = string.ascii_uppercase[1::2]
        w = ''.join([x for x in word if x in odd_letters])
        return len(w)

    @staticmethod
    def amount_alphabetical(word):
        j = len(word)
        for i in range(1, len(word)):
            if ord(word[i]) < ord(word[i - 1]):
                j -= 1
        return j

    @staticmethod
    def scrabble_score(word):
        scrabble_scores = {'A': 1, 'B': 3, 'C': 5, 'D': 2, 'E': 1, 'F': 4, 'G': 3, 'H': 4, 'I': 1, 'J': 4, 'K': 3,
                           'L': 3, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 2, 'S': 2, 'T': 2, 'U': 4, 'V': 4,
                           'W': 5, 'X': 8, 'Y': 8, 'Z': 4}
        return sum([scrabble_scores[x] for x in word])

    @staticmethod
    def position_in_alphabet(word):
        return sum([ord(x) - 64 for x in word])


if __name__ == '__main__':
    ws = WordSorter(['AANVRAAG', 'ACTIVIST', 'AFBAKBROODJE', 'BAVIAAN', 'BEGINPERIODE',
                     'CELLO', 'CHIRURG', 'DEBAT', 'EINDIG', 'GROOTVIZIER', 'KERNSPLIJTING',
                     'KIEVIET', 'KOPPEL', 'LEGER', 'LENIGEN', 'LETTERGREPEN', 'LEVENSLANG',
                     'PENTA', 'PRACHTIG', 'PREDICAAT', 'RING', 'STEL', 'TELEVISIEGIDS',
                     'TIRADE', 'TWEEBAANSWEGEN', 'UITBESTEDEN', 'VIS', 'QUOTA'])

    for method in ['nr_letters', 'nr_vowels', 'nr_first_half', 'nr_last_half',
                   'position_up_to_alphabetical', 'amount_alphabetical',
                   'nr_even_letters', 'nr_odd_letters', 'scrabble_score',
                   'position_in_alphabet']:
        print('*** {} ***'.format(method))
        ws.sort_words(method)
        print()
