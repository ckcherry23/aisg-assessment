"""Module to handle API requests with retry logic."""

from typing import Any, Dict
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry  # type: ignore
from src.config import Config
from src.exceptions.api_request_exception import APIRequestException


class APIClient:
    """Class to handle API requests with retry logic.

    Attributes:
        config (:obj:`Config`): Configuration object containing API retry parameters.
        session (:obj:`Session`): HTTP session object initialized with retry strategy.
    """

    def __init__(self, config: Config | None = None) -> None:
        """Initializes an instance of APIClient.

        Args:
            config (:obj:`Config`, optional): Configuration object. Defaults to None,
                                              in which case a default configuration
                                              (`Config()`) is used.
        """
        self.config = config or Config()
        self.session = self._init_session()

    def _init_session(self) -> Session:
        """Initializes a session with retry strategy.

        Returns:
            :obj:`Session`: Initialized HTTP session object.
        """
        session = Session()
        (
            max_retries,
            status_forcelist,
            backoff_factor,
        ) = self.config.get_api_retry_params()
        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=status_forcelist,
            backoff_factor=backoff_factor,  # type: ignore
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        return session

    def get_api_url(self, base_url: str, path: str) -> str:
        """Constructs the full API URL.

        Args:
            base_url (str): Base URL of the API.
            path (str): Path of the API endpoint.

        Returns:
            str: The full API URL.
        """
        return f"{base_url}/{path}"

    def get_headers(self, token: str) -> Dict[str, str]:
        """Constructs headers for API requests.

        Args:
            token (str): Access token for authorization.

        Returns:
            dict: Headers dictionary with authorization information.
        """
        return {"Authorization": f"Bearer {token}"}

    def post(
        self, url: str, headers: Dict[str, str], payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Sends a POST request with retry logic.

        Args:
            url (str): The API endpoint URL.
            headers (dict): Headers for the POST request.
            payload (dict): Payload for the POST request.

        Returns:
            dict: JSON response from the API.

        Raises:
            APIRequestException: If the API request fails with a non-200 status code.
        """
        response = self.session.post(url, headers=headers, json=payload)
        if response.status_code == 200:  # pylint: disable=no-else-return
            return response.json()
        else:
            raise APIRequestException(
                f"API request failed with status code {response.status_code}: {response.text}"
            )
