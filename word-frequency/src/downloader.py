import urllib.request


class Downloader:
    """Class to handle downloading of the text file."""

    @staticmethod
    def download_text_file(url) -> str:
        """Download the text file from the specified URL."""
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
