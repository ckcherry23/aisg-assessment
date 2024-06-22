from src.text_generator import TextGenerator
from src.config import Config
from src.api_client import APIClient


def main():
    """Main function to demonstrate text generation based on user input.

    This function initializes an API client with configuration from 'config.yaml',
    creates a TextGenerator instance using the API client, prompts the user for an input prompt,
    generates text based on the prompt using the TextGenerator, and prints the generated text.

    Example:
        $ python3 -m src.main
        Enter the prompt input: Once upon a time
        Once upon a time, there was a...

    Raises:
        Exception: If there's an issue loading configuration or making API requests.
    """
    api_client = APIClient(Config(config_file="./config.yaml"))
    text_generator = TextGenerator(api_client=api_client)

    input_prompt = input("Enter the prompt input: ")
    generated_text = text_generator.generate_text(input_prompt)
    print(generated_text)


if __name__ == "__main__":
    main()
