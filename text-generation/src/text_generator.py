class TextGenerator:
    """Class to handle text generation using Hugging Face API.

    Attributes:
        api_client (:obj:`APIClient`): An instance of APIClient used for API communication.
        config (:obj:`Config`): Configuration object containing API and model parameters.
    """

    def __init__(self, api_client) -> None:
        """Initialize TextGenerator instance.

        Args:
            api_client (:obj:`APIClient`): An instance of APIClient used for API communication.
        """
        self.api_client = api_client
        self.config = api_client.config

    def generate_text(self, prompt) -> str:
        """
        Generates text continuation using the Hugging Face Inference API.

        Args:
            prompt (str): The input text to generate continuation for.

        Returns:
            str: The generated text.

        Raises:
            Exception: If there's an issue with API request or response handling.
        """
        base_url, model_id = self.config.get_hugging_face_api_details()
        url = self.api_client.get_api_url(
            base_url=base_url,
            path=model_id,
        )
        headers = self.api_client.get_headers(self.config.hugging_face_api_token)

        payload = {
            "inputs": prompt,
            "parameters": self.config.get_hugging_face_model_parameters(),
        }

        response_json = self.api_client.post(url, headers, payload)
        generated_text = response_json[0]["generated_text"]
        return generated_text
