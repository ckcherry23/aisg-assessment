# Text Generation 

This project uses the Hugging Face Inference API with GPT-2 for text generation.

<!-- TODO: Add demo video -->

## Requirements

1. Python 3.11 or higher
2. Hugging Face API token

## Setup

1. Clone the repository and navigate to the `text-generation` directory:
    ```sh
    git clone https://github.com/ckcherry23/aisg-assessment.git
    cd aisg-assessment/text-generation
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Create a `.env` file and add your Hugging Face API token:
    ```txt
    HUGGING_FACE_API_TOKEN=<your-token>
    ```
   You can refer to the `env.template` file for reference.

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Run the program:
    ```sh
    python3 -m src.main
    ```

## Usage

The program will prompt you to enter an input text and generate text based on the input. 

## Configuration

You can configure the Hugging Face model and API settings in the `config.yaml` file. The following configuration options are available:

| Key | Description | Default Value | Is Required | 
| --- | ----------- | ------------- | ----------- |
| `hugging_face.base_url` | String: Base URL for the Hugging Face API | - | Yes |
| `hugging_face.model_id` | String: Model ID for the Hugging Face model | - | Yes |
| `hugging_face.parameters.max_new_tokens` | Int: Maximum number of tokens to generate | `50` | No |
| `hugging_face.parameters.num_return_sequences` | Int: Number of sequences to generate | `1` | No |
| `hugging_face.parameters.temperature` | Float: Sampling temperature for the model | `0.8` | No |
| `api_client.retry.max_retries` | Int: Maximum number of retries for API requests | `3` | No |
| `api_client.retry.status_forcelist` | List<Int>: List of HTTP status codes to retry | `[500, 502, 503, 504]` | No |
| `api_client.retry.backoff_factor` | Float: Backoff factor for exponential backoff | `0.5` | No |
