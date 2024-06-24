import unittest
from unittest.mock import patch, MagicMock
from src.api_client import APIClient
from src.config import Config
from src.exceptions.api_request_exception import APIRequestException


class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.mock_config = MagicMock(Config)
        self.mock_config.hugging_face_api_token = "mock-token"
        self.mock_config.get_api_retry_params.return_value = (
            "mock-parameter-1",
            "mock-parameter-2",
            "mock-parameter-3",
        )
        self.api_client = APIClient(config=self.mock_config)

    @patch("requests.Session.post")
    def test_post_success(self, mock_post: MagicMock):
        url = "https://mock-url.com"
        headers = {"Authorization": "Bearer mock-token"}
        payload = {"inputs": "Once upon a time", "parameters": "mock-parameters"}

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_post.return_value = mock_response

        response = self.api_client.post(url, headers, payload)
        self.assertEqual(response, {"key": "value"})

    @patch("requests.Session.post")
    def test_post_failure(self, mock_post: MagicMock):
        url = "https://mock-url.com"
        headers = {"Authorization": "Bearer mock-token"}
        payload = {"inputs": "Once upon a time", "parameters": "mock-parameters"}

        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        with self.assertRaises(APIRequestException):
            self.api_client.post(url, headers, payload)

    def test_get_api_url(self):
        base_url = "https://mock-url.com"
        path = "mock-path"

        url = self.api_client.get_api_url(base_url, path)
        self.assertEqual(url, "https://mock-url.com/mock-path")

    def test_get_headers(self):
        headers = self.api_client.get_headers("mock-token")
        self.assertEqual(headers, {"Authorization": "Bearer mock-token"})


if __name__ == "__main__":
    unittest.main()
