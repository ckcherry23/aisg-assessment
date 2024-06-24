"""Module to test the text_generator module."""

import unittest
from unittest.mock import MagicMock
from src.text_generator import TextGenerator
from src.api_client import APIClient
from src.config import Config


class TestTextGenerator(unittest.TestCase):
    """Class to test the TextGenerator class."""

    def setUp(self):
        """Initializes the mock config and mock API client objects."""
        self.mock_config = MagicMock(Config)
        self.mock_config.get_hugging_face_api_details.return_value = (
            "base_url",
            "model_id",
        )
        self.mock_config.hugging_face_api_token = "token"

        self.mock_api_client = MagicMock(APIClient)
        self.mock_api_client.config = self.mock_config
        self.text_generator = TextGenerator(api_client=self.mock_api_client)

    def test_generate_text(self):
        """Test the generate_text method."""
        prompt = "Once upon a time"
        mock_response = [{"generated_text": "Once upon a time, there was a..."}]

        self.mock_api_client.post.return_value = mock_response

        generated_text = self.text_generator.generate_text(prompt)

        self.mock_api_client.post.assert_called_once()
        self.assertEqual(generated_text, "Once upon a time, there was a...")


if __name__ == "__main__":
    unittest.main()
