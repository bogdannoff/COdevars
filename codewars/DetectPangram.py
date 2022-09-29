import string
import unittest


def is_pangram(str):
    abc = set(list('abcdefghijklmnopqrstuvwxyz'))
    return abc == abc.intersection(set(list(str.lower())))

def is_pangram_2(str):
    return set(string.ascii_lowercase).issubset(set(list(str.lower())))


class TestMyCase(unittest.TestCase):

    def test_1(self):
        sentence = 'The quick brown fox jumps over the lazy dog'
        self.assertEqual(is_pangram(sentence), True)
        self.assertEqual(is_pangram_2(sentence), True)

    def test_2(self):
        sentence = 'The quick fox jumps over the lazy dog'
        self.assertEqual(is_pangram(sentence), False)
        self.assertEqual(is_pangram_2(sentence), False)

    def test_3(self):
        sentence = 'ABCDEFGHijklmnopqrstuvwxyz 123456'
        self.assertEqual(is_pangram(sentence), True)
        self.assertEqual(is_pangram_2(sentence), True)

    def test_4(self):
        sentence = '123456'
        self.assertEqual(is_pangram(sentence), False)
        self.assertEqual(is_pangram_2(sentence), False)

