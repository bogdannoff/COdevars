import unittest


def count_change(money, coins):
    ways = [1] + [0] * money
    for coin in coins:
        for i in range(coin, money + 1):
            ways[i] += ways[i - coin]
    return ways[money]

class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(count_change(4, [1,2]), 3)

    def test_2(self):
        self.assertEqual(count_change(10, [5,2,3]), 4)

if __name__ == '__main__':
    count_change(10, [1])
    count_change(10, [2])
    count_change(10, [1, 2])
