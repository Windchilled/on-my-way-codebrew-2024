import json
from dateutil import parser

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.incident import *

def runAddIncident(json_data):

    json_dict = json.load(json_data)
    print(json_dict)
    post_date = '2024-07-13T00:00:00.000Z'
    location_name = "Lincoln Square, Melbourne, VIC, Australia"
    x_coord = 6.314
    y_coord = 5.203
    post_time = parser.parse(post_date)
    desc = "i am an incident number 4!!"
    severity = 8
    emergency_service = "N/A"
    addIncident(location_name, x_coord, y_coord, post_time, desc, severity, emergency_service)
    return json_data
