"""Module for APIRequestException."""


class APIRequestException(Exception):
    """Exception raised for API request failures."""

    def __init__(self, message: str) -> None:
        """Initializes an APIRequestException.

        Args:
            message (str): Error message.
        """
        super().__init__(message)
