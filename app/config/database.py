from decouple import config
from pymongo import MongoClient

client = MongoClient(config("MONGO_URL"))

db = client.prompthub
