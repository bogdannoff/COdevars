import unittest


def strip_comments(strng, markers):
    l = strng.split('\n')
    for j, x in enumerate(l):
        for i, ch in enumerate(x):
            if ch in markers:
                l[j] = x[:i].rstrip()
                break
    return '\n'.join(l)


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']),
                         'apples, pears\ngrapes\nbananas')

    def test_2(self):
        self.assertEqual(strip_comments(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')
