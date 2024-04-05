from flask import Flask,request,jsonify
from flask import Blueprint
from controllers import test

incident = Blueprint("incident",__name__)

@incident.route('/add', methods = ['POST','GET'])
def addIncident():
    data = request.json
    result = test.test(data)
    return jsonify(result)