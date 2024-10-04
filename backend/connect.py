from flask_pymongo import pymongo
from pymongo.mongo_client import MongoClient
import os

MONGO_URI = os.config['MONGO_URI']

client = MongoClient(MONGO_URI)
db = client.get_database('app')
users = pymongo.collection.Collection(db, 'users')