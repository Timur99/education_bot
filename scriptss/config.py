import os
import json

def load_credentials(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data


DB_CREDENTIALS = 'credentials/postgresql.json'

TGRM_BOT_CREDENTIALS = 'credentials/tg.json'

OPENAI_API = 'credentials/cred_llm.json'


"""
import os
import json


def load_credentials(filepath):
    if 'paths.json' in filepath and 'dags' in next(os.walk('.'))[1]:
        filepath = os.path.join('dags', filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

# Clickhouse
DB_CREDENTIALS = 'credentials/postgresql.json'

# files
#PATHS = 'paths.json'
#PATHS = 'credentials/'

# TGRM_BOT_CREDENTIALS
TGRM_BOT_CREDENTIALS = 'credentials/tg_bot.json'


"""