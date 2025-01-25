from sqlalchemy import create_engine
from parliament import Base

import json

with open("reader/config.json") as config_file:
    config = json.load(config_file)

DATABASE_URL = f"postgresql://{config['db_user']}:{config['db_password']}@{config['db_host']}/{config['db_name']}"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)


