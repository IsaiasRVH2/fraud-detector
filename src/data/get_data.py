import sys
import os
import yaml

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import src.config.settings as settings

from kaggle.api.kaggle_api_extended import KaggleApi


def get_data(source: str, destination: str):
    """
    Downloads dataset files from a specified source to a destination path.

    This function uses the Kaggle API to download dataset files and
    automatically unzips them in the specified destination folder.

    Args:
        source (str): The source identifier of the dataset to download.
            This is typically a Kaggle dataset path.
        destination (str): The local directory path where the downloaded
            files will be saved.

    Returns:
        None: This function doesn't return any value.

    Dependencies:
        Requires the Kaggle API (kg) to be properly configured with
        appropriate authentication.
    """
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(source, path=destination, unzip=True)

    return None

with open("./config/data_config.yaml", "r") as file:
    data = yaml.safe_load(file)
source = data["source"]
destination = data["destination"]
get_data(source=source, destination=destination)