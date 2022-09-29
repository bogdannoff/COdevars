import unittest

def digital_root(n):
    val = n
    base = 10
    while val // base > 0:
        total = 0
        while val > 0:
            total += val % base
            val = val // base
        val = total
    return val

def digital_root_2(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


class TestMyCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(digital_root(16),7)
        self.assertEqual(digital_root_2(16),7)

    def test_2(self):
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root_2(942), 6)

    def test_3(self):
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root_2(132189), 6)

    def test_4(self):
        self.assertEqual(digital_root(493193), 2)
        self.assertEqual(digital_root_2(493193), 2)

