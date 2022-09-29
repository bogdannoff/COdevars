import unittest


class RomanNumerals:

    @staticmethod
    def to_roman(d):
        dct = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = ''
        while d > 0:
            divider = 10**(len(str(d))-1)
            x = d // divider
            if x > 0 and x < 4:
                res += dct[divider] * x
            elif x == 4:
                res += dct[divider]
                res += dct[5 * divider]
            elif x == 5:
                res += dct[5*divider]
            elif x > 5 and x < 9:
                res += dct[5 * divider]
                res += dct[divider] * (x - 5)
            elif x == 9:
                res += dct[divider]
                res += dct[divider*10]
            d = d % divider
        return res

    @staticmethod
    def from_roman(r):
        dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = 0
        mx = 0
        for i in r[::-1]:
            s += dct[i]*(-1 if dct[i] < mx else 1)
            mx = max(dct[i], mx)
        return s


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC')

    def test_2(self):
        self.assertEqual(RomanNumerals.to_roman(2008), 'MMVIII')

    def test_3(self):
        self.assertEqual(RomanNumerals.to_roman(1666), 'MDCLXVI')

    def test_4(self):
        self.assertEqual(RomanNumerals.from_roman('MCMXC'), 1990)

    def test_5(self):
        self.assertEqual(RomanNumerals.from_roman('MMVIII'), 2008)

    def test_6(self):
        self.assertEqual(RomanNumerals.from_roman('MDCLXVI'), 1666)

