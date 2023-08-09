from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_KEY = os.environ.get("SERVICE_KEY")
VERSION = os.environ.get("VERSION")

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

PGADMIN__EMAIL = os.environ.get("PGADMIN_EMAIL")
PGADMIN__PASS = os.environ.get("PGADMIN_PASS")
