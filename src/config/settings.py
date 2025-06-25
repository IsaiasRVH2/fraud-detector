import dotenv
import os

dotenv.load_dotenv()
# Define the settings class
class Settings:
    """
    Settings class for managing Kaggle API credentials.

    This class loads Kaggle authentication credentials from environment variables
    to facilitate dataset downloads and API interactions.

    Attributes:
        kaggle_username (str): The Kaggle username from environment variable 'KAGGLE_USERNAME',
                               defaults to 'default_username' if not set.
        kaggle_key (str): The Kaggle API key from environment variable 'KAGGLE_KEY',
                          defaults to 'default_key' if not set.

    Example:
        ```
        settings = Settings()
        username = settings.kaggle_username
        api_key = settings.kaggle_key
        ```
    """
    def __init__(self):
        self.kaggle_username = os.getenv("KAGGLE_USERNAME", "default_username")
        self.kaggle_key = os.getenv("KAGGLE_KEY", "default_key")
        
def load_settings():
    settings = Settings()
    return settings