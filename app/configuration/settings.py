import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('POSTGRES_DB')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
DB_USER = os.getenv('POSTGRES_USER')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_HOST = os.getenv('POSTGRES_HOST')


DATABASE_URL = f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
BASE_DIR = Path(__file__).parent.parent.parent
JSON_FILE = BASE_DIR / 'init.json'

DB_CONFIG = {
    "connections": {
        "default": DATABASE_URL
    },
    "apps": {
        "models": {
            "models": ['app.database.tables.tables'] + ['aerich.models']
        }
    }
}



