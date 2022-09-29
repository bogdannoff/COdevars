import unittest


def equal_sides(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(equal_sides([1,2,3,4,3,2,1]), 3)

    def test_2(self):
        self.assertEqual(equal_sides([1,100,50,-51,1,1]), 1)

    def test_3(self):
        self.assertEqual(equal_sides([20,10,-80,10,10,15,35]), 0)
