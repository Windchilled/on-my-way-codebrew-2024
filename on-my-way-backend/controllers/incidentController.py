import json
import bson
from dateutil import parser
from flask import jsonify
from datetime import datetime

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.incident import *

def runAddIncident(json_data):
    for i in json_data.values():
        if i == None:
            return jsonify({'error': "An incident field is missing"}), 500
        
    time_now = datetime.now()
    dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")

    severity = json_data['severity']
    latitude = json_data['latitude']
    longitude = json_data['longitude']
    dateTime = dt_string
    desc = json_data['description']
    
    addIncident(severity,latitude,longitude,dateTime,desc)
    return json_data
