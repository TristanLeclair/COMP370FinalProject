import argparse
import logging

import numpy as np
import pandas as pd
from src.common.logging_utils import add_logging_args, setup_root_logger

global logger


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Split a file into multiple files with a given number of lines."
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        required=True,
        help="Input file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        required=False,
        help="Output tsv file.",
        default="data/processed/split_data.tsv",
    )

    add_logging_args(parser)

    args = parser.parse_args()

    return args.input, args.output, args.log_level, args.deep_logging


def main():
    input_file, output_file, log_level, deep_logging = parse_args()
    np.random.seed(42)

    setup_root_logger(logging, log_level, deep_logging)
    logger = logging.getLogger(__name__)

    logger.info("Loading data...")
    df = pd.read_json(input_file)
    df_clean = df.copy()
    df_clean.dropna(inplace=True)

    # remove removed articles
    df_clean = df_clean[df_clean["source"] != "[Removed]"]
    # randomly sample 200 articles
    df_sampled = df_clean.sample(n=200)

    logger.info("Writing data...")

    logger.info(df_sampled.head())

    df_sampled.to_csv(output_file, sep="\t", index=False)

    pass


if __name__ == "__main__":
    main()
