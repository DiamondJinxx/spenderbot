from pymongo import MongoClient
from config import db_config

client = MongoClient(db_config.mongo_uri)

