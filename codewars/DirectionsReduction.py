import unittest


def dirReduc(arr):
    for i in range(len(arr)-1):
        if arr[i] == "NORTH" and arr[i+1] == "SOUTH" or\
           arr[i] == "SOUTH" and arr[i + 1] == "NORTH" or\
           arr[i] == "WEST" and arr[i + 1] == "EAST" or\
           arr[i] == "EAST" and arr[i + 1] == "WEST":
            return dirReduc(arr[:i]+arr[i+1+1:len(arr)])
    return arr


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])

    def test_2(self):
        self.assertEqual(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])

