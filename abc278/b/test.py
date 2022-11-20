from main import *

import unittest


class TestAtCoder(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(7), 13)


if __name__ == '__main__':
    unittest.main()
