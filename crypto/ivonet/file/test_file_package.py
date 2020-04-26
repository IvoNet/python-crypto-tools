import unittest

from ivonet.file import *


class TestFileActions(unittest.TestCase):
    def test_something(self):
        self.assertTrue(get_txt_dir().endswith("../files/txt"))

    def test_file_exists(self):
        self.assertTrue(os.path.exists(get_txt_file("2_letters_no_diacritics.txt")))


if __name__ == '__main__':
    unittest.main()
