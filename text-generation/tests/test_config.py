"""Module to test the config module."""

from typing import Any
import unittest
from unittest.mock import patch, mock_open
import os
from src.config import Config


class TestConfig(unittest.TestCase):
    """Class to test the Config class."""

    @patch.dict(os.environ, {"HUGGING_FACE_API_TOKEN": "test_token"})
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="""
hugging_face:
  base_url: "https://api-inference.huggingface.co/models"
  model_id: "gpt2"
  parameters:
    max_new_tokens: 50
    num_return_sequences: 1
    temperature: 0.8
api_client:
  retry:
    max_retries: 3
    status_forcelist: [500, 502, 503, 504]
    backoff_factor: 0.5
""",
    )
    @patch("os.path.exists", return_value=True)
    def test_config_loading(
        self, mock_exists: bool, mock_file: Any
    ):  # pylint: disable=unused-argument
        """Test the loading of the configuration file and environment variables."""
        config = Config(config_file="dummy.yaml")
        self.assertEqual(config.hugging_face_api_token, "test_token")
        self.assertEqual(
            config.get_hugging_face_api_details(),
            ("https://api-inference.huggingface.co/models", "gpt2"),
        )
        self.assertEqual(config.get_api_retry_params(), (3, [500, 502, 503, 504], 0.5))
        self.assertEqual(
            config.get_hugging_face_model_parameters(),
            {"max_new_tokens": 50, "num_return_sequences": 1, "temperature": 0.8},
        )


if __name__ == "__main__":
    unittest.main()
