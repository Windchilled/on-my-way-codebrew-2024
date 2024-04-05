#import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ashhastings:Qq3ydvtj67ywtDZI@cluster0.acct40j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['OnMyWay']
collection = db['Incidents']