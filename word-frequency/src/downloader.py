import urllib.request


class Downloader:
    """Class to handle downloading of text files."""

    @staticmethod
    def download_text_file(url) -> str:
        """Download the text file from the specified URL.

        Args:
            url (str): The URL of the text file to download.

        Returns:
            str: The content of the downloaded text file as a string.

        Raises:
            URLError: If there's an issue with the URL or the network.
        """
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
