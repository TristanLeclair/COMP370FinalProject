import argparse
import logging
import os

from src.common.logging_utils import add_logging_args, setup_root_logger
from src.common.collect import get_from_api
from src.common.json_utils import load_json, output_to_path

global logger


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def parse_args():
    parser = argparse.ArgumentParser(
        description="A script to collect articles from newsapi.org",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # add path to folder containing json files with keywords
    parser.add_argument(
        "-i",
        type=dir_path,
        help="Folder containing json files with keywords",
    )

    parser.add_argument(
        "-o", type=str, help="Output folder", default="data/raw/movies/"
    )

    # add ignore cache argument
    parser.add_argument(
        "-c",
        "--ignore-cache",
        dest="ignore_cache",
        action="store_true",
        help="Ignore the cache",
        default=False,
    )

    add_logging_args(parser)
    args = parser.parse_args()
    return args.i, args.o, args.ignore_cache, args.log_level, args.deep_logging


def main():
    input_folder, output_folder, ignore_cache, log_level, deep_logging = parse_args()

    setup_root_logger(logging, log_level, deep_logging)
    logger = logging.getLogger(__name__)

    if not os.path.exists(input_folder):
        raise Exception(f"Folder {input_folder} does not exist")

    # loop over all files in input folder
    for filename in os.listdir(input_folder):
        # check if file is a json file
        if filename.endswith(".json"):
            # load json file
            logger.info(f"Loading {filename}")
            # extract keywords
            file_path = os.path.join(input_folder, filename)
            with open(file_path) as f:
                keywords = load_json(f)
                data = get_from_api(keywords, use_cache=not ignore_cache, pages=50)
                output_to_path(os.path.join(output_folder, filename), data)

            pass

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pass


if __name__ == "__main__":
    main()
