import os
import json

from pathlib import Path

import telethon
import sqlite3 as sql


path_to_telegram_api = Path(__file__).parent / 'telegram_api.json'
with open(path_to_telegram_api, 'r') as f:
    api = json.load(f)
    api_id = api['API_ID']
    api_hash = api['API_HASH']



client = telethon.TelegramClient(
    'listener', 
    api_id, 
    api_hash
)

