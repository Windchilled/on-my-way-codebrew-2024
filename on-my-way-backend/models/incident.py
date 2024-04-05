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
        "x-coord" : x_coord,
        "y-coord" : y_coord,
        "date-time" : post_time,
        "description" : desc,
        "severity" : severity,
        "emergency-service" : emergency_service
    }

    collection.insert_one(new_incident)
    

def getIncidents():
    
    allIncidents = []
    for eachIncident in collection.find({}, {}): 
        eachIncident['_id'] = str(eachIncident['_id'])
        allIncidents.append(eachIncident)
    #print(allIncidents)
    return allIncidents


def getIncidentDetails(_id):
    incident = collection.find_one({"_id" : _id},{"_id" : 0})
    return incident

def deleteIncident(_id):
    result = collection.delete_one({"_id" : _id})
    return result