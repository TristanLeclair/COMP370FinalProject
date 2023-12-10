import argparse

from src.common.requestutils import make_query_or, make_query_and
from src.common.collect import get_from_newsapi
from src.common.json_utils import output_to_path, load_json

KEYWORDS = [
    "Taylor Swift | The Eras Tour",
    "The Exorcist: Believer",
    "PAW Patrol: The Mighty Movie",
    "Killers of the Flower Moon",
    "Five Nights at Freddy’s",
    "Priscilla",
    "Saw X",
    "The Creator",
    "After Death",
    "The Marvels",
]


def parse_args():
    """Parse command line arguments.
    Parse command line arguments and return them.
    i and k are mutually exclusive.

    Returns:
        tuple: A tuple containing:
            - args.i: Input file
            - args.k: List of keywords
            - args.o: Output file
            - args.a: Use AND instead of OR
    """
    parser = argparse.ArgumentParser(
        description="A script to collect articles from newsapi.org",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-i",
        type=argparse.FileType("r"),
        help="Json file containing a list of keywords",
    )
    group.add_argument(
        "-k",
        nargs="+",
        help="List of keywords",
        default=KEYWORDS,
    )

    parser.add_argument(
        "-o",
        type=argparse.FileType("w"),
        help="Output file",
        default="data/raw/articles.json",
    )

    parser.add_argument(
        "-a",
        action="store_true",
        help="Use AND instead of OR",
        default=False,
    )

    args = parser.parse_args()

    return (args.i, args.k, args.o, args.a)


def main():
    (input_file, keywords, output_file, use_and) = parse_args()
    if input_file:
        KEYWORDS = load_json(input_file)
    elif keywords:
        KEYWORDS = keywords
    else:
        raise ValueError("Need to either provide a file or a list of keywords")

    if use_and:
        query = make_query_and(KEYWORDS)
    else:
        query = make_query_or(KEYWORDS)

    data = get_from_newsapi(query)

    output_to_path(output_file, data.json())


if __name__ == "__main__":
    main()
