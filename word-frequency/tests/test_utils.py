"""Module for testing the utility functions in the src.utils module."""

import unittest
from src.utils import ordinal


class TestUtils(unittest.TestCase):
    """Class to test the utility functions."""

    def test_ordinal(self):
        """Test the ordinal function."""
        self.assertEqual(ordinal(1), "1st")
        self.assertEqual(ordinal(2), "2nd")
        self.assertEqual(ordinal(3), "3rd")
        self.assertEqual(ordinal(4), "4th")
        self.assertEqual(ordinal(11), "11th")
        self.assertEqual(ordinal(12), "12th")
        self.assertEqual(ordinal(13), "13th")
        self.assertEqual(ordinal(21), "21st")
        self.assertEqual(ordinal(22), "22nd")
        self.assertEqual(ordinal(23), "23rd")
        self.assertEqual(ordinal(101), "101st")
        self.assertEqual(ordinal(111), "111th")
        self.assertEqual(ordinal(0), "0th")
        self.assertEqual(ordinal(1000), "1000th")


if __name__ == "__main__":
    unittest.main()
