from dateutil import parser
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ashhastings:Qq3ydvtj67ywtDZI@cluster0.acct40j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['OnMyWay']
collection = db['Incidents']


def addIncident(severity, lat, long, post_time, desc):
    new_incident = {
        "severity" : severity,
        "coordinates" : [lat,long],
        "date-time" : post_time,
        "description" : desc,
    }

    collection.insert_one(new_incident)
    

def getIncidents():
    
    allIncidents = []
    for eachIncident in collection.find({}, {}): 
        eachIncident['_id'] = str(eachIncident['_id'])
        data = {
            type : "Feature",
            "geometry" : {
                type : "Point",
                "coordinates" : eachIncident["coordinates"]
            } ,
            "properties" : {
                "database_id" : eachIncident["_id"],
                "severity" : eachIncident["severity"],
                "dateTime" : eachIncident["dateTime"],
                "description" : eachIncident["description"]
            }
        }
        allIncidents.append(data)
    #print(allIncidents)
    return allIncidents


def getIncidentDetails(_id):
    incident = collection.find_one({"_id" : _id},{"_id" : 0})
    return incident

def deleteIncident(_id):
    result = collection.delete_one({"_id" : _id})
    return result