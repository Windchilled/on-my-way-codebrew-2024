#import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ashhastings:Qq3ydvtj67ywtDZI@cluster0.acct40j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['OnMyWay']
collection = db['Incidents']

document = {"name":"ash","city":"melbourne"}
insert_doc = collection.insert_one(document)

print(f"inserted doc ID: {insert_doc.inserted_id}")
client.close()


''' Send a ping to confirm a successful connection
#try:
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#    print(e)'''