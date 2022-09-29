import unittest
from collections import Counter


def first_non_repeating_letter(s):
    c = Counter(s.lower())
    for x in s:
        if c[x.lower()] == 1:
            return x
    return ''


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')

