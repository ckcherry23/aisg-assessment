"""Main module test cases."""

import unittest
from unittest.mock import patch, MagicMock
import os
from src.main import main


class TestMain(unittest.TestCase):
    """Class to test the main module."""

    @patch.dict(os.environ, {"HUGGING_FACE_API_TOKEN": "test_token"})
    @patch("builtins.input", return_value="Life is a box of")
    @patch("builtins.print")
    @patch(
        "src.text_generator.TextGenerator.generate_text",
        return_value="""Life is a box of chocolates that are given to people in
various stages of their illness as a means of providing warmth to their loved
ones.""",
    )
    def test_main(
        self,
        mock_generate_text: MagicMock,
        mock_print: MagicMock,
        mock_input: MagicMock,  # pylint: disable=unused-argument
    ):
        """Test the main function with mocks."""

        main()

        mock_generate_text.assert_called_once_with("Life is a box of")
        mock_print.assert_called_once_with(
            """Generated Text: Life is a box of chocolates that are given to people in
various stages of their illness as a means of providing warmth to their loved
ones.""",
            flush=True,
        )


if __name__ == "__main__":
    unittest.main()
