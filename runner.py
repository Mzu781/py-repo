# test_math_operations.py
import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(2.5, 2.5), 5.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-3, -7), 4)
        self.assertEqual(subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(2.5, 2), 5.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7.5, 2.5), 3.0)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
