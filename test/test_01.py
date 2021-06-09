import unittest
import math_func


class TestMathFunc(unittest.TestCase):

    def test_ap_bp(self):
        self.assertEqual(math_func.sum2(10, 1), 21)

    def test_an_bp(self):
        self.assertEqual(math_func.sum2(-5, 10), 15)

    def test_an_bn(self):
        self.assertEqual(math_func.sum2(-5, -10), -15)

    def test_ap_bn(self):
        self.assertEqual(math_func.sum2(5, -10), 0)


if __name__ == '__main__':
    unittest.main()
