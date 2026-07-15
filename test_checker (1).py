"""
test_checker.py
-----------------
Simple tests for checker.py. Run with:

    python -m unittest test_checker.py
"""

import unittest
from checker import check_password_strength


class TestPasswordStrengthChecker(unittest.TestCase):

    def test_short_password_is_weak(self):
        result = check_password_strength("Ab1!")
        self.assertEqual(result["rating"], "Weak")

    def test_common_password_is_weak(self):
        result = check_password_strength("password")
        self.assertEqual(result["rating"], "Weak")

    def test_strong_password(self):
        result = check_password_strength("Tr0ub4dor&Zebra")
        self.assertEqual(result["rating"], "Strong")

    def test_medium_password(self):
        result = check_password_strength("abcdefgh1")
        self.assertIn(result["rating"], ("Weak", "Medium"))


if __name__ == "__main__":
    unittest.main()
