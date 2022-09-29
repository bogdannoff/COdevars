import unittest


def rgb(r, g, b):
    return hex(max(min(r, 255), 0)).replace('0x', '').rjust(2, '0').upper() + \
           hex(max(min(g, 255), 0)).replace('0x', '').rjust(2, '0').upper() + \
           hex(max(min(b, 255), 0)).replace('0x', '').rjust(2, '0').upper()


def rgb2(r, g, b):
    f = lambda x: max(min(x, 255), 0)
    # res = ('{:02X}'*3).format(f(r), f(g), f(b))
    res = f'{f(r):02X}{f(g):02X}{f(b):02X}'
    return res


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(rgb(-1, 100, 300), '0064FF')
        self.assertEqual(rgb2(-1, 100, 300), '0064FF')

    def test_2(self):
        self.assertEqual(rgb(148, 0, 211), '9400D3')
        self.assertEqual(rgb2(148, 0, 211), '9400D3')
