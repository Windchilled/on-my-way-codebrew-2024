from flask import Flask,request,jsonify
from flask import Blueprint
#from controllers import test
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controllers.incidentController import *
#from controllers.recieveIncidentController import *


incident = Blueprint("incident",__name__)

@incident.route('/add', methods = ['POST','GET'])
def addIncident():
    json_data = request.json
    #result = test.test(data)
    result = runAddIncident(json_data)
    return jsonify(result)

@incident.route('/allIncidents', methods = ['POST','GET'])
def retrieveIncidents():
    result = retrieveAllIncidents()
    return jsonify(result)

@incident.route('/incidentDetails', methods = ['POST','GET'])
def retrieveincidentDetails():

    _id = request.json

    result = retrieveIncident(_id)

    return jsonify(result)
