import json


def getDBUrl():
    with open("reader/config.json") as config_file:
        config = json.load(config_file)

    DATABASE_URL = f"postgresql://{config['db_user']}:{config['db_password']}@{config['db_host']}/{config['db_name']}"
    return DATABASE_URL