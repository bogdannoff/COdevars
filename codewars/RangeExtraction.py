import unittest


def res_append(first, second, res):
    if first == second:
        res.append(str(first))
    elif abs(first - second) == 1:
        res.append(f'{str(first)},{str(second)}')
    else:
        res.append(f'{str(first)}-{str(second)}')
    return res


def solution(l):
    res = []
    first = l[0]
    second = l[0]
    for i in range(1, len(l)):
        if abs(l[i]-l[i-1]) == 1:
            second = l[i]
        else:
            res_append(first, second, res)
            first = l[i]
            second = l[i]
    res_append(first, second, res)
    return ','.join(res)



class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]),
                         '-10--8,-6,-3-1,3-5,7-11,14,15,17-20')

