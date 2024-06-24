import unittest
from src.downloader import Downloader


class TestDownloader(unittest.TestCase):
    def test_download_text_file(self):
        url = "https://www.gutenberg.org/cache/epub/16317/pg16317.txt"
        downloader = Downloader()
        text = downloader.download_text_file(url)
        self.assertIn("Project Gutenberg", text)


if __name__ == "__main__":
    unittest.main()
