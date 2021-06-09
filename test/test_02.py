import unittest
import math_func


class TestMathFunc(unittest.TestCase):
    def test_print_hi(self):
        self.assertEqual(math_func.print_hi('Vova'), 'Hi, Vova')
