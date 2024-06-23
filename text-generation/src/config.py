import os
from typing import Any, Dict, List, Tuple
import yaml
import pydash
from dotenv import load_dotenv


class Config:
    """Configuration class to load environment variables and constants.

    Attributes:
        hugging_face_api_token (str): API token for Hugging Face API loaded from environment variables.
        config_data (dict): Parsed configuration data from the YAML config file.
    """

    def __init__(self, config_file="config.yaml") -> None:
        """Initialize Config instance.

        Args:
            config_file (str, optional): Path to the configuration YAML file. Defaults to "config.yaml".

        Raises:
            Exception: If the Hugging Face API token is not set in the environment or if the config file is not found.
        """
        self._load_env_vars()
        self._load_config_file(config_file)

    def _load_env_vars(self) -> None:
        """Load environment variables, including the Hugging Face API token.

        Raises:
            Exception: If the Hugging Face API token is not set in the environment.
        """
        load_dotenv()
        self.hugging_face_api_token = os.getenv("HUGGING_FACE_API_TOKEN")

        if not self.hugging_face_api_token:
            raise Exception("Hugging Face API token is not set in the environment")

    def _load_config_file(self, config_file) -> None:
        """Load constants from the specified config file.

        Args:
            config_file (str): Path to the configuration YAML file.

        Raises:
            Exception: If the config file is not found or if there is an error loading the YAML content.
        """
        if not os.path.exists(config_file):
            raise Exception(f"Config file not found at {config_file}")

        with open(config_file, "r") as file:
            try:
                config_data = yaml.safe_load(file)
            except yaml.YAMLError as exc:
                raise Exception(f"Error loading config file: {exc}")

        self.config_data = config_data

    def get_hugging_face_api_details(self) -> Tuple[str, str]:
        """Get the base URL and model ID for the Hugging Face API.

        Returns:
            tuple: A tuple containing the base URL (str) and model ID (str).
        """
        base_url = self._get_config_value("hugging_face.base_url")
        model_id = self._get_config_value("hugging_face.model_id")
        return base_url, model_id

    def get_api_retry_params(self) -> Tuple[int, List[int], float]:
        """Get the retry parameters for API requests.

        Returns:
            tuple: A tuple containing maximum retries (int), status codes to force retry (list of int),
                   and backoff factor (float).
        """
        max_retries = self._get_config_value("api_client.retry.max_retries", default=3)
        status_forcelist = self._get_config_value(
            "api_client.retry.status_forcelist", default=[500, 502, 503, 504]
        )
        backoff_factor = self._get_config_value(
            "api_client.retry.backoff_factor", default=0.5
        )
        return max_retries, status_forcelist, backoff_factor

    def get_hugging_face_model_parameters(self) -> Dict[str, Any]:
        """Get the model parameters for the Hugging Face API.

        Returns:
            dict: A dictionary containing model parameters.
                  Keys: "max_new_tokens" (int), "num_return_sequences" (int), "temperature" (float).
        """
        max_new_tokens = self._get_config_value(
            "hugging_face.parameters.max_new_tokens", default=50
        )
        num_return_sequences = self._get_config_value(
            "hugging_face.parameters.num_return_sequences", default=1
        )
        temperature = self._get_config_value(
            "hugging_face.parameters.temperature", default=0.8
        )
        return {
            "max_new_tokens": max_new_tokens,
            "num_return_sequences": num_return_sequences,
            "temperature": temperature,
        }

    def _get_config_value(self, key: str, default: Any = None) -> Any:
        """Get the value associated with the specified key from the config file.

        Args:
            key (str): Key in dot notation (e.g., "hugging_face.base_url") to retrieve the value.
            default (Any, optional): Default value to return if the key is not found. Defaults to None.

        Raises:
            KeyError: If the key is not found in the config file.

        Returns:
            Any: Value associated with the specified key.
        """
        value = pydash.get(self.config_data, key, default)
        if value is None:
            raise KeyError(f"Key value not found in config file: {key}")
        return value
