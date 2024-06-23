import re
from collections import Counter
from typing import List, Tuple


class DataProcessor:
    """Class to process text and calculate word frequencies."""

    @staticmethod
    def clean_text(text) -> str:
        """Clean the text by removing punctuation and converting to lower case."""
        text = re.sub(r"[^\w\s]", "", text)
        text = text.lower()
        return text

    @staticmethod
    def compute_word_frequencies(text) -> Counter:
        """Compute the frequency of each word in the text using an efficient approach."""
        words = text.split()
        word_counts = Counter(words)
        return word_counts

    @staticmethod
    def get_top_words(word_counts, start_rank, end_rank) -> List[Tuple[str, int]]:
        """Get words ranked from start_rank to end_rank by frequency."""
        # `Counter.most_common()` uses `heapq.nlargest()` for time complexity O(n log k)
        # where n is the number of unique words and k is the number of most common words tracked
        # Reference: https://github.com/python/cpython/blob/1ba0bb21ed4eb54023fdfccc9cb20be8fff946b1/Lib/collections/__init__.py#L620
        most_common_words = word_counts.most_common(end_rank)
        return most_common_words[start_rank - 1 : end_rank]
