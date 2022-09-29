import unittest
from math import gcd


def solution(l):
    m = min(l)
    for i in range(len(l)):
        if l[i] % m != 0:
            m = l[i] % m
    return len(l)*m


def solution2(a):
    return gcd(*a) * len(a)


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([6, 9, 21]), 9)
        self.assertEqual(solution2([6, 9, 21]), 9)

    def test_2(self):
        self.assertEqual(solution([3, 6, 12]), 9)
        self.assertEqual(solution2([3, 6, 12]), 9)

    def test_3(self):
        self.assertEqual(solution([1, 21, 55]), 3)
        self.assertEqual(solution2([1, 21, 55]), 3)

    def test_4(self):
        self.assertEqual(solution([9]), 9)
        self.assertEqual(solution2([9]), 9)

    def test_5(self):
        self.assertEqual(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 144, 144, 1]), 17)
        self.assertEqual(solution2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 144, 144, 1]), 17)

