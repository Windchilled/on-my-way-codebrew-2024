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
    
    allIncidents = []
    for eachIncident in collection.find({}, {"_id":0}): 
        allIncidents.append(eachIncident)
    #print(allIncidents)
    return allIncidents


def getIncidentDetails(_id):
    incident = collection.find_one(_id)
    print("the id" , _id)
    print("the incident",incident)
    #for x in collection.find(_id):
    #    print("here i am", x)
    for x in collection.find({"_id":_id},{"id" : 0}):
        print(x)

    return collection.find({"_id":_id},{"id" : 0})
    # Nothing here yet
    