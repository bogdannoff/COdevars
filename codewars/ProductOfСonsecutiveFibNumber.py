import unittest


def product_of_fib(val):
    n1, n2 = 0, 1
    while val > n1 * n2:
        n1, n2 = n2, n1+n2
    return [n1, n2, val == n1 * n2]


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(product_of_fib(714), [21, 34, True])

    def test_2(self):
        self.assertEqual(product_of_fib(800), [34, 55, False])

