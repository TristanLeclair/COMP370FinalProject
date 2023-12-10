import argparse
import logging
from typing import List, Tuple

from requests_cache import CachedSession
from src.common.collect import get_from_newsapi
from src.common.json_utils import load_json, output_to_path
from src.common.logging_utils import add_logging_args, setup_root_logger
from src.common.requestutils import make_query_and, make_query_or

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

global logger


def parse_args() -> Tuple[argparse.FileType, List[str], str, bool, bool, str, bool]:
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
        type=str,
        help="Output file",
        default="data/raw/articles.json",
    )

    parser.add_argument(
        "-a",
        action="store_true",
        help="Use AND instead of OR",
        default=False,
    )

    add_logging_args(parser)

    # add ignore cache argument
    parser.add_argument(
        "-c",
        "--ignore-cache",
        dest="ignore_cache",
        action="store_true",
        help="Ignore the cache",
        default=True,
    )

    args = parser.parse_args()

    return (
        args.i,
        args.k,
        args.o,
        args.a,
        args.ignore_cache,
        args.log_level,
        args.deep_logging,
    )


def use_cache(name: str) -> CachedSession:
    """Use a cached session.
    Returns:
        CachedSession: A cached session.
    """

    return CachedSession(
        name + "_cache",
        ignored_parameters=["apiKey"],
        expire_after=3600,
        backend="filesystem",
    )


def main():
    global logger
    (
        input_file,
        keywords,
        output_file,
        use_and,
        use_caching,
        log_level,
        deep_logging,
    ) = parse_args()

    setup_root_logger(logging, log_level, deep_logging)
    logger = logging.getLogger(__name__)

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

    session = use_cache("newsapi") if use_caching else None

    data = get_from_newsapi(query, session=session)

    output_to_path(output_file, data.json())

    logger.info(f'Collected {data.json()["totalResults"]} articles')


if __name__ == "__main__":
    main()
