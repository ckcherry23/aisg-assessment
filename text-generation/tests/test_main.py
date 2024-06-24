import unittest
from unittest.mock import patch
from src.main import main
from unittest.mock import MagicMock


class TestMain(unittest.TestCase):
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
        mock_input: MagicMock,
    ):

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
