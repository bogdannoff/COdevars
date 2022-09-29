import unittest


def queue(q, n):
    t = [0]*n
    for x in q:
        t[0] += x
        t.sort()
    return t[n-1]


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(queue([5,3,4], 1), 12)

    def test_2(self):
        self.assertEqual(queue([2,3,10], 2), 12)

    def test_3(self):
        self.assertEqual(queue([10,2,3,3,5,1], 3), 10)
