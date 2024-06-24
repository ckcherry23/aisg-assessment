"""Module for testing the main function."""

import unittest
from io import StringIO
from unittest.mock import patch
from src.main import main


class TestMain(unittest.TestCase):
    """Class to test the main function."""

    @patch("sys.stdout", new_callable=StringIO)
    def test_main_output(self, mock_stdout: StringIO):
        """Test the output of the main function."""
        main()
        output = mock_stdout.getvalue()
        expected = """Words ranked from 10th to 20th by frequency:
you: 1461
for: 1340
as: 1198
be: 1178
not: 1152
he: 1071
with: 1035
his: 1027
are: 991
i: 946
this: 935
"""
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
