import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    BOT_TOKEN = "7598148687:AAEmfJIR9jwlXJkQ-_CfQQLtf209i3q41zM"
    API_ID = 22792918
    API_HASH = "ff10095d2bb96d43d6eb7a7d9fc85f81"
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
