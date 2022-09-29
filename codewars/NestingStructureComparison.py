import unittest


def same_structure_as1(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if isinstance(l1[i], list) != isinstance(l2[i], list):
            return False
        if isinstance(l1[i], list) and not same_structure_as(l1[i], l2[i]):
            return False
    return True

def same_structure_as(l1, l2):
    if isinstance(l1, list) != isinstance(l2, list):
        return False
    if isinstance(l1, list):
        if len(l1) != len(l2):
            return False
        for i in range(len(l1)):
            if not same_structure_as(l1[i], l2[i]):
                return False
    return True

class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ), True)

    def test_2(self):
        self.assertEqual(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ]), True)

    def test_3(self):
        self.assertEqual(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ]), False)

    def test_4(self):
        self.assertEqual(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ), False)

    def test_5(self):
        self.assertEqual(same_structure_as([],1 ), False)
