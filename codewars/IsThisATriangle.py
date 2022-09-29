import unittest


def is_triangle(a, b, c):
    return all([a < b + c, b < a + c, c < a + b])


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_triangle(1, 2, 2), True)

    def test_2(self):
        self.assertEqual(is_triangle(7, 2, 2), False)
