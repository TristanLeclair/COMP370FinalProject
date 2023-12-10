import argparse

from src.common.logging_utils import add_logging_args


def parse_args():
    parser = argparse.ArgumentParser(
        description="A script to extract information from a newsapi.org query",
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
    pass


if __name__ == "__main__":
    main()
