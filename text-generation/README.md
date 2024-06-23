# Text Generation 

This program uses the Hugging Face Inference API with GPT-2 for text generation.

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
    source venv/bin/activate # Use 'venv\Scripts\activate' on Windows
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

The program will prompt you to enter an input text and output generated text based on the input using text completion.

## Configuration

You can configure the Hugging Face model and API settings in the `config.yaml` file. The default configuration file can be accessed [here](config.yaml). The following configuration options are available: 

| Key | Description | Type | Required | Default Value |
| --- | ----------- | ---- | -------- | ------------- |
| `hugging_face.base_url` | Base URL for the Hugging Face API (without trailing slash) | String | Yes | - |
| `hugging_face.model_id` | Model ID for the Hugging Face model | String | Yes | - |
| `hugging_face.parameters.max_new_tokens` | Maximum number of tokens to generate | Int | No | 50 |
| `hugging_face.parameters.num_return_sequences` | Number of sequences to generate | Int | No | 1 |
| `hugging_face.parameters.temperature` | Sampling temperature for the model | Float | No | 0.8 |
| `api_client.retry.max_retries` | Maximum number of retries for API requests | Int | No | 3 |
| `api_client.retry.status_forcelist` | List of HTTP status codes to retry | List[Int] | No | [500, 502, 503, 504] |
| `api_client.retry.backoff_factor` | Backoff factor for exponential backoff | Float | No | 0.5 |
