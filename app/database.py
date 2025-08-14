import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")

with open(CONFIG_PATH) as f:
    config = json.load(f)

required_keys = ["db_user", "db_password", "db_host", "db_port", "db_name"]
for key in required_keys:
    if key not in config:
        raise KeyError(f"Missing key in config.json: {key}")

DATABASE_URL = (
    f"postgresql+psycopg2://{config['db_user']}:{config['db_password']}"
    f"@{config['db_host']}:{config['db_port']}/{config['db_name']}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
