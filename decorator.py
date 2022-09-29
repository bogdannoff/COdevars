import datetime
import unittest


def multiple_exec(*dargs, **dkwargs):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            attempts = dkwargs['attempts']
            while attempts>0:
                try:
                    return func(*args, **kwargs)
                except:
                    print(f'attempts: {attempts}')
                    attempts -=1
        return wrapper2
    return wrapper1

def exec_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        print('Execution time: ', end-start)
        return result
    return wrapper

@exec_time
@multiple_exec(attempts=5)
def div(a, b):
    return a/b


class TestDecorators(unittest.TestCase):
    def test_1(self):
        self.assertEqual(div(10,5),2)
        self.assertEqual(div(10, 0), None)
        self.assertEqual(multiple_exec(attempts=3)(div)(2, 5), 0.4)

