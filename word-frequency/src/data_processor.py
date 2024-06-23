"""Module to process text and calculate word frequencies."""

import re
from collections import Counter
from typing import List, Tuple


class DataProcessor:
    """Class to process text and calculate word frequencies."""

    @staticmethod
    def clean_text(text: str) -> str:
        """Clean the text by removing punctuation and converting to lower case.

        Args:
            text (str): The input text to be cleaned.

        Returns:
            str: The cleaned text with punctuation removed and converted to lower case.
        """
        text = re.sub(r"[^\w\s]", "", text)
        text = text.lower()
        return text

    @staticmethod
    def compute_word_frequencies(text: str) -> Counter[str]:
        """Compute the frequency of each word in the text using an efficient approach.

        Args:
            text (str): The input text to compute word frequencies from.

        Returns:
            Counter: A Counter object with words as keys and their frequencies as values.
        """
        words = text.split()
        word_counts = Counter(words)
        return word_counts

    @staticmethod
    def get_top_words(
        word_counts: Counter[str], start_rank: int, end_rank: int
    ) -> List[Tuple[str, int]]:
        """Get words ranked from start_rank to end_rank by frequency.

        Args:
            word_counts (Counter): A Counter object with words as keys and their frequencies as
                                   values.
            start_rank (int): The starting rank of the words to be retrieved.
            end_rank (int): The ending rank of the words to be retrieved.

        Returns:
            List[Tuple[str, int]]: A list of tuples containing words and their frequencies,
            ranked from start_rank to end_rank.
        """
        # `Counter.most_common()` uses `heapq.nlargest()` for time complexity O(n log k)
        # where n is the number of unique words and k is the number of most common words tracked
        # Reference: https://github.com/python/cpython/blob/1ba0bb21ed4eb54023fdfccc9cb20be8fff946b1/Lib/collections/__init__.py#L620 pylint: disable=line-too-long
        most_common_words = word_counts.most_common(end_rank)
        return most_common_words[start_rank - 1 : end_rank]
