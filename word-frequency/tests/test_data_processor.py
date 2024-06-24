"""Module to test the data_processor module."""

import unittest
from collections import Counter
from src.data_processor import DataProcessor


class TestProcessor(unittest.TestCase):
    """Class to test the DataProcessor class."""

    def setUp(self):
        """Initializes the DataProcessor and text for testing."""
        self.data_processor = DataProcessor()
        self.text = "Hello world! Hello universe. Hello everyone."
        self.clean_text = "hello world hello universe hello everyone"

    def test_clean_text(self):
        """Test the clean_text method."""
        cleaned = self.data_processor.clean_text(self.text)
        self.assertEqual(cleaned, self.clean_text)

    def test_compute_word_frequencies(self):
        """Test the compute_word_frequencies method."""
        word_counts = self.data_processor.compute_word_frequencies(self.clean_text)
        expected_counts = Counter(
            {"hello": 3, "world": 1, "universe": 1, "everyone": 1}
        )
        self.assertEqual(word_counts, expected_counts)

    def test_get_top_words(self):
        """Test the get_top_words method."""
        word_counts = Counter({"hello": 3, "world": 1, "universe": 1, "everyone": 1})
        top_words = self.data_processor.get_top_words(word_counts, 2, 3)
        expected_top_words = [("world", 1), ("universe", 1)]
        self.assertEqual(top_words, expected_top_words)


if __name__ == "__main__":
    unittest.main()
