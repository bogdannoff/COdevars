import unittest


def which_in(array1, array2):
    return sorted({item1 for item1 in array1 if any(item1 in item2 for item2 in array2)})


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(which_in(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]), ["arp", "live", "strong"])

    def test_2(self):
        self.assertEqual(which_in(["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]), ["arp"])
