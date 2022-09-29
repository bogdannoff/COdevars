import math
import unittest


def persistence(n):
    return persistence(math.prod([int(ch) for ch in str(n)])) + 1 if n >= 10 else 0


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(persistence(39), 3)

    def test_2(self):
        self.assertEqual(persistence(999), 4)
