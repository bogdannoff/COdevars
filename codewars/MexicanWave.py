import unittest


def mexican_wave(str):
    return ["".join(map(lambda x: (x[1].upper() if x[0] == i else x[1]), enumerate(str))) for i in range(len(str)) if str[i].isalpha()]


def mexican_wave2(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(mexican_wave('hello'), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
        self.assertEqual(mexican_wave2('hello'), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])

