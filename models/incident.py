from dateutil import parser
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ashhastings:Qq3ydvtj67ywtDZI@cluster0.acct40j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['OnMyWay']
collection = db['Incidents']


def addIncident(location, x_coord, y_coord, post_time, desc, severity, emergency_service):
    new_incident = {
        "location" : location,
        "x_coord" : x_coord,
        "y_coord" : y_coord,
        "datetime" : post_time,
        "description" : desc,
        "severity" : severity,
        "emergency_service" : emergency_service
    }

    collection.insert_one(new_incident)
    client.close()

def getIncidents():
    # Nothing here yet
    print("hi")

def getIncidentDetails():
    # Nothing here yet
    print("hi 2")