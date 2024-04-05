from flask import Flask,request
from flask_pymongo import PyMongo
import database

app = Flask(__name__)


app.config['MONGO_URI'] = database.uri

mongo = PyMongo(app)

from routers.incidentsRouter import incident

app.register_blueprint(incident,url_prefix = "/")


@app.route("/",methods = ['GET','POST'])

def home():
    return "hi"


if __name__ == '__main__':
    app.run(debug=True,port=8000)