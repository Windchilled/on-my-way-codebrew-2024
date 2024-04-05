import json
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
        
    print(json_data['location'])
    time_now = datetime.now()
    dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")

    location_name = json_data['location']
    x_coord = json_data['x-coord']
    y_coord = json_data['y-coord']
    post_time = dt_string
    desc = json_data['description']
    severity = json_data['severity']
    emergency_service = json_data['emergency-service']
    addIncident(location_name, x_coord, y_coord, post_time, desc, severity, emergency_service)
    return json_data
