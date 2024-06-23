from src.downloader import Downloader
from src.data_processor import DataProcessor
from src.utils import ordinal


def main():
    # Configuration
    src_url = "https://www.gutenberg.org/cache/epub/16317/pg16317.txt"
    start_rank = 10
    end_rank = 20

    downloader = Downloader()
    text = downloader.download_text_file(src_url)

    data_processor = DataProcessor()
    clean_text = data_processor.clean_text(text)
    word_counts = data_processor.compute_word_frequencies(clean_text)

    top_words = data_processor.get_top_words(word_counts, start_rank, end_rank)

    print(
        f"Words ranked from {ordinal(start_rank)} to {ordinal(end_rank)} by frequency:"
    )
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
