import unittest
from functools import reduce
from math import sqrt


def solution(m, n):
    res = []
    for num in range(m, n+1):
        s = 0
        for x in range(1, int(sqrt(num))+1):
            if num%x == 0:
                s += x**2
                if num/x != x:
                    s += int(num/x)**2
        sq = sqrt(s)
        if int(sq) == sq:
            res.append([num, s])
    return res

class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution(1, 250), [[1, 1], [42, 2500], [246, 84100]])

    def test_2(self):
        self.assertEqual(solution(42, 250), [[42, 2500], [246, 84100]])

