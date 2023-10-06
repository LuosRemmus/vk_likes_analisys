from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
MEDIA_FILEPATH = os.environ.get("MEDIA_FILEPATH")
