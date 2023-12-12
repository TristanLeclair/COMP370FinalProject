import argparse
import logging

import pandas as pd
from src.common.coding_headers import Headers
from src.common.logging_utils import add_logging_args, setup_root_logger

global logger


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Split a file into multiple files with a given number of lines."
    )
    parser.add_argument(
        "-i", "--input", dest="input", required=True, help="tsv of codings"
    )
    add_logging_args(parser)

    args = parser.parse_args()

    return args.input, args.output, args.log_level, args.deep_logging


def import_data(input_file):
    """Read data."""
    return pd.read_csv(input_file, sep="\t")


def clean_data(df):
    """Clean data."""
    df_clean = df.copy()
    # only keep columns we need
    df_clean = df_clean[
        [
            Headers.title.value,
            Headers.description.value,
            Headers.coder1.value,
            Headers.movie1.value,
            Headers.topic1.value,
            Headers.coder2.value,
            Headers.movie2.value,
            Headers.topic2.value,
            Headers.final_movie.value,
            Headers.final_topic.value,
        ]
    ]
    # clean strings
    # remove leading and trailing whitespace
    # remove multiple spaces
    df_clean = df_clean.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return df_clean


def movie_counts(df):
    """Count movies."""
    df_counts = df.copy()
    # count unique final movies, some articles have multiple movies
    # split on comma and count unique movies
    df_counts["final_movie"] = df_counts["final_movie"].str.split(",")
    # count unique movies
    counts = df_counts["final_movie"].value_counts()

    return counts


def compile_topics(df):
    """Compile topics per movie."""
    df_topics = df.copy()
    # ignore Not_mentioned and Not_relevant
    df_topics = df_topics[
        (df_topics["final_movie"] != "Not_mentioned")
        & (df_topics["final_movie"] != "Not_relevant")
    ]
    # group by movie
    df_topics = df_topics.groupby("final_movie")
    # get topics for each movie
    topics = df_topics["final_topic"].apply(list)
    return topics


def characterize_topics(df):
    """Characterize topics per movie."""
    df_topics = df.copy()
    # ignore Not_mentioned and Not_relevant
    df_topics = df_topics[
        (df_topics["final_movie"] != "Not_mentioned")
        & (df_topics["final_movie"] != "Not_relevant")
    ]
    df_topics = df_topics.groupby(Headers.final_topic.value)
    # for each topic, get the tf-idf
    # return topics
    pass


def main():
    input_file, output_file, log_level, deep_logging = parse_args()

    setup_root_logger(logging, log_level, deep_logging)
    logger = logging.getLogger(__name__)

    logger.info("Reading input file...")

    df = import_data(input_file)

    logger.info("Cleaning data...")

    df_clean = clean_data(df)

    logger.info("Counting movies...")

    counts = movie_counts(df_clean)

    logger.info(f"counts: {counts}")

    logger.info("Compiling topics...")

    topics = compile_topics(df_clean)

    logger.info("Characterizing topics...")

    tf_idfs = characterize_topics(df_clean)

    pass


if __name__ == "__main__":
    main()
