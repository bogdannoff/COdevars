"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,
containing distinct letters - each taken only once - coming from s1 or s2.
"""
import unittest


def two_to_one(s1, s2):
    return ''.join(sorted(set(s1+s2)))


class TestMyCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(two_to_one('xyaabbbccccdefww', 'xxxxyyyyabklmopq'), 'abcdefklmopqwxy')

    def test_2(self):
        self.assertEqual(two_to_one('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'), 'abcdefghijklmnopqrstuvwxyz')
