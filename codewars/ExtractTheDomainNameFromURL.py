import re
import unittest


def get_domain(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('.')[0]


def get_domain_re(url):
    return re.search(r'(https?://)?(www\.)?(?P<domain>[\w-]+)\.', url).group('domain')


class TestMyCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_domain('http://github.com/carbonfive/raygun'), 'github')
        self.assertEqual(get_domain_re('http://github.com/carbonfive/raygun'), 'github')

    def test_2(self):
        self.assertEqual(get_domain('http://www.zombie-bites.com'), 'zombie-bites')
        self.assertEqual(get_domain_re('http://www.zombie-bites.com'), 'zombie-bites')

    def test_3(self):
        self.assertEqual(get_domain('https://www.cnet.com'), 'cnet')
        self.assertEqual(get_domain_re('https://www.cnet.com'), 'cnet')
