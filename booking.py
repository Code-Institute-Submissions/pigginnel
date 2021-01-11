import os
import pymongo
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "ginnelPig"
COLLECTION = "reservations"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

new_doc = {"first": "Jane", "last": "Doe", "date": "10/02/2021", "slot": "1", "covers": "6", "email": "test2@gmail.com"} # noqa

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
