# Word Frequency 

This program downloads a text file from Project Gutenberg and prints the top 10th to 20th words (inclusive) by frequency.

https://github.com/ckcherry23/aisg-assessment/assets/68203159/726048c0-fd77-4c71-a46f-a4134d534664

## Requirements

1. Python 3.11 or higher

## Setup

1. Clone the repository and navigate to the `word-frequency` directory:
    ```sh
    git clone https://github.com/ckcherry23/aisg-assessment.git
    cd aisg-assessment/word-frequency
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate # Use 'venv\Scripts\activate' on Windows
    ```

3. Run the program:
    ```sh
    python3 -m src.main
    ```

## Approach

1. Download the text file from Project Gutenberg.
2. Read the text file and tokenize the words. A word is defined as a sequence of characters separated by whitespace. Punctuation marks are removed and the words are converted to lowercase.
3. Count the frequency of each word. The `collections.Counter` class is used to count the frequency of each word.
4. Retrieve the top 20 words by frequency. The `Counter.most_common(k)` method is used to retrieve the top 20 words by frequency. This method uses a heap queue to efficiently retrieve the most common words in O(n log k) time, where n is the number of unique words and k is the number of words to retrieve.
5. Print the 10th to 20th words by frequency.

## Configuration

The URL of the text file, the start and end indices of the words to print, and the number of words to print can be configured with the `src/main.py` file as constants.

## Testing

To run the tests, use the following command:
```sh
python3 -m unittest
```
