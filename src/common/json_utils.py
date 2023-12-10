import json
import os


def load_json(input_file):
    """Load json from file."""
    return json.load(input_file)


def output_to_path(path: str, data: dict):
    """Output data to path.
    Will verify that the path exists and then output the data to it.
    If the path does not exist, it will create the folder structure."""

    if path:
        output_dir = os.path.dirname(path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
