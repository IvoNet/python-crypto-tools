import os
import re

# TODO: not working yet
from ivonet.file import get_txt_file, read_txt_file_current_path_no_diacritics


class DictionaryRegexer:
    def __init__(self):
        self.words = read_txt_file_current_path_no_diacritics("OpenTaal-210G-basis-gekeurd.txt")

    def find_words_with_pattern(self, pattern: str) -> [str]:
        regexp = self.pattern_to_regexp(pattern)
        return re.findall(regexp, self.words, re.IGNORECASE)

    def pattern_to_regexp(self, pattern):
        return ''.join(['[\w]*' if char == '*' else char for char in pattern])


if __name__ == '__main__':
    dr = DictionaryRegexer()
    print(len(dr.words))
    all_words = dr.find_words_with_pattern('kamer*plant')
    print(all_words)
