"""This module contains the test cases for math_operations."""

import unittest
from math_operations import add, subtract, multiply, divide, exponentiate

class TestMathOperations(unittest.TestCase):
    """Test cases for the math_operations module."""

    def test_add(self):
        """Test the add function from math_operations."""
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(2.5, 2.5), 5.0)
        with self.assertRaises(ValueError):
            add("a", 2)

    def test_subtract(self):
        """Test the subtract function from math_operations."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-3, -7), 4)
        self.assertEqual(subtract(5.5, 2.5), 3.0)
        with self.assertRaises(ValueError):
            subtract("a", 2)

    def test_multiply(self):
        """Test the multiply function from math_operations."""
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(2.5, 2), 5.0)
        with self.assertRaises(ValueError):
            multiply("a", 2)

    def test_divide(self):
        """Test the divide function from math_operations."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7.5, 2.5), 3.0)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ValueError):
            divide("a", 2)

    def test_exponentiate(self):
        """Test the exponentiate function from math_operations."""
        self.assertEqual(exponentiate(2, 3), 8)
        self.assertEqual(exponentiate(3, 0), 1)
        self.assertEqual(exponentiate(2.5, 2), 6.25)
        with self.assertRaises(ValueError):
            exponentiate("a", 2)

if __name__ == '__main__':
    unittest.main()