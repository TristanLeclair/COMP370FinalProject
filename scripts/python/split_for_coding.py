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


def import_data(input_file):
    """Import data."""
    return pd.read_json(input_file)


def clean_data(df):
    """Clean data.
    Remove rows with missing values.
    Remove removed articles.
    """
    df_clean = df.copy()
    df_clean.dropna(inplace=True)
    # remove removed articles
    df_clean = df_clean[df_clean["source"] != "[Removed]"]
    return df_clean


def sample_data(df, n=200):
    """Sample data.
    Sample 200 articles.

    Return sampled data and non-sampled data.
    """
    df_sampled = df.sample(n=n)

    df_non_sampled = df.copy()
    df_non_sampled.drop(df_sampled.index, inplace=True)  # pyright: ignore

    return df_sampled, df_non_sampled


def log_data(df_sampled, df_non_sampled, logger):
    """Log data."""
    logger.info(f"Number of sampled articles: {len(df_sampled)}")
    logger.info(df_sampled.head())
    logger.info(f"Number of non-sampled articles: {len(df_non_sampled)}")
    logger.info(df_non_sampled.head())


def create_final_data(df_sampled, df_non_sampled):
    df_final = df_sampled.copy()
    # add non-sampled data to end of sampled data
    df_final._append(df_non_sampled)
    return df_final


def output_data(df, output_file):
    df.to_csv(output_file, sep="\t", index=False)


def main():
    input_file, output_file, log_level, deep_logging = parse_args()
    np.random.seed(42)

    setup_root_logger(logging, log_level, deep_logging)
    logger = logging.getLogger(__name__)

    logger.info("Loading data...")

    df = import_data(input_file)

    logger.info("Cleaning data...")

    df_clean = clean_data(df)

    logger.info("Sampling data...")

    df_sampled, df_non_sampled = sample_data(df_clean)

    log_data(df_sampled, df_non_sampled, logger)

    logger.info("Compiling final data...")

    df_final = create_final_data(df_sampled, df_non_sampled)

    logger.info("Outputting data...")

    output_data(df_sampled, output_file)

    final_output_file = output_file.split(".")[0] + "_final.tsv"
    output_data(df_final, final_output_file)

    pass


if __name__ == "__main__":
    main()
