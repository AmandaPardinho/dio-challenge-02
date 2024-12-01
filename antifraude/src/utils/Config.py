import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT_DOC")
    KEY = os.getenv("KEY")
    CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")


