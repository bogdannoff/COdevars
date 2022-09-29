import unittest


def rot13(s):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc13 = {x: abc[(13+i)%len(abc)] for i, x in enumerate(abc)}
    def f(x):
        if x.isalpha():
            return (abc13[x.lower()].upper() if x.isupper() else (abc13[x.lower()]))
        else:
            return x
    return ''.join(list(map(f, s)))



class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(rot13('test'), 'grfg')

    def test_2(self):
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%')

