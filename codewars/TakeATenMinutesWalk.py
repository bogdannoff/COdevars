import unittest
from collections import Counter

"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early 
to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens 
with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter 
strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each 
letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will 
return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
and will, of course, return you to your starting point. Return false otherwise.
"""


def is_it_ten_minutes_walk(l):
    counter = Counter(map(lambda el: el.lower(), l))
    return counter['n'] == counter['s'] and counter['e'] == counter['w'] and len(l) == 10


def is_it_ten_minutes_walk_2(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


class TestMyCase(unittest.TestCase):

    def test_1(self):
        path = ['n', 'e', 'n', 'w', 'w', 's', 's', 's', 'e', 'n']
        self.assertEqual(is_it_ten_minutes_walk(path), True)
        self.assertEqual(is_it_ten_minutes_walk_2(path), True)

    def test_2(self):
        path = ['n', 'e', 'n', 'w', 'w', 's', 's', 's', 'e', 'e']
        self.assertEqual(is_it_ten_minutes_walk(path), False)
        self.assertEqual(is_it_ten_minutes_walk_2(path), False)

    def test_3(self):
        path = ['n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's']
        self.assertEqual(is_it_ten_minutes_walk(path), True)
        self.assertEqual(is_it_ten_minutes_walk_2(path), True)

    def test_4(self):
        path = ['n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's', 'n', 'e', 'n', 'w', 'w', 's', 's', 's', 'e', 'n']
        self.assertEqual(is_it_ten_minutes_walk(path), False)
        self.assertEqual(is_it_ten_minutes_walk_2(path), False)

    def test_5(self):
        path = ['w', 'w', 's', 's', 's', 'e', 'n']
        self.assertEqual(is_it_ten_minutes_walk(path), False)
        self.assertEqual(is_it_ten_minutes_walk_2(path), False)

