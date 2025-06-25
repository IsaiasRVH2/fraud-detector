import kaggle as kg
#from src.config.settings import settings
import os
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
    kg.api.authenticate()  # Ensure the Kaggle API is authenticated
    kg.api.dataset_download_files(source, path=destination, unzip=True)

    return None