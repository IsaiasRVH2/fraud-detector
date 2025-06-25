import dotenv
import os
# Load environment variables from .env file
dotenv.load_dotenv()

# Define the settings class
class Settings:
    def __init__(self):
        self.kaggle_username = os.getenv("KAGGLE_USERNAME", "default_username")
        self.kaggle_key = os.getenv("KAGGLE_KEY", "default_key")
        
settings = Settings()