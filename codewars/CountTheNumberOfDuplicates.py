"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric
digits that occur more than once in the input string. The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.
"""
import unittest
from collections import Counter


def count_duplicates(s):
    return len(dict(filter(lambda x: x[1] > 1, Counter(s.lower()).items())))


class TestMyCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_duplicates('abcde'), 0)

    def test_2(self):
        self.assertEqual(count_duplicates('aabBcde'), 2)

    def test_3(self):
        self.assertEqual(count_duplicates('Indivisibilities'), 2)
