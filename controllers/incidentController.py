import json
from dateutil import parser
from flask import jsonify

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.incident import *

def runAddIncident(json_data):
    for i in json_data.values():
        if i == None:
            return jsonify({'error': "A field contains missing data"}), 500
        
    print(json_data['location'])

    location_name = json_data['location']
    x_coord = json_data['x-coord']
    y_coord = json_data['y-coord']
    post_time = parser.parse(json_data['date-time'])
    desc = json_data['description']
    severity = json_data['severity']
    emergency_service = json_data['emergency-service']
    addIncident(location_name, x_coord, y_coord, post_time, desc, severity, emergency_service)
    return json_data
