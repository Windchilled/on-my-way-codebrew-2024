from dateutil import parser
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ashhastings:Qq3ydvtj67ywtDZI@cluster0.acct40j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['OnMyWay']
collection = db['Incidents']


def addIncident():
    post_date = '2024-07-13T00:00:00.000Z'


    # Parse JSON into variables:

    location_name = "Lincoln Square, Melbourne, VIC, Australia"
    x_coord = 6.314
    y_coord = 5.203
    post_time = parser.parse(post_date)
    desc = "i am an incident!!"
    severity = 8
    emergency_service = "N/A"

    new_incident = {
        "location" : location_name,
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