"""Module to test the downloader module."""

import unittest
from src.downloader import Downloader


class TestDownloader(unittest.TestCase):
    """Class to test the Downloader class."""

    def test_download_text_file(self):
        """Test the download_text_file method."""
        url = "https://www.gutenberg.org/cache/epub/16317/pg16317.txt"
        downloader = Downloader()
        text = downloader.download_text_file(url)
        self.assertIn("Project Gutenberg", text)


if __name__ == "__main__":
    unittest.main()
