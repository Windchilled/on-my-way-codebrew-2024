from flask import Flask;
from flask import Blueprint;

incident = Blueprint("incident",__name__)

@incident.route('/add')
def addIncident():
    return "added"