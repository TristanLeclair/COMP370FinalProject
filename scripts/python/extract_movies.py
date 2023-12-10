import argparse
import logging

from src.common.logging_utils import add_logging_args, setup_root_logger
from src.common.json_utils import load_json, output_to_path

global logger


def parse_args():
    parser = argparse.ArgumentParser(
        description="A script to extract articles from a newsapi.org query",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i",
        type=argparse.FileType("r"),
        help="A list of articles in json format",
    )

    parser.add_argument(
        "-o",
        type=str,
        help="Output file",
        default="data/processed/movies.json",
    )

    add_logging_args(parser)

    args = parser.parse_args()

    return args.i, args.o, args.log_level, args.deep_logging


def main():
    input_file, output_file, log_level, deep_logging = parse_args()

    setup_root_logger(logging, log_level, deep_logging)
    logger = logging.getLogger(__name__)

    data = load_json(input_file)

    logger.info("Extracting movies from articles")

    totalArticles = data[0]["totalResults"]

    logger.info(f"Found {totalArticles} articles with keywords")

    extracted_articles = []
    for page in data:
        for article in page["articles"]:
            source = article["source"]["name"]
            title = article["title"]
            description = article["description"]
            url = article["url"]
            publishedAt = article["publishedAt"]
            content = article["content"]
            extracted = {
                "source": source,
                "title": title,
                "description": description,
                "url": url,
                "publishedAt": publishedAt,
                "content": content,
            }
            extracted_articles.append(extracted)

    logger.info(f"Extracted {len(extracted_articles)} articles")

    # check for duplicates
    unique_articles = []
    for article in extracted_articles:
        if article not in unique_articles:
            unique_articles.append(article)

    logger.info(f"Found {len(unique_articles)} unique articles")

    output_to_path(output_file, unique_articles)

    pass


if __name__ == "__main__":
    main()
