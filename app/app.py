from flask import Flask, jsonify, Response
import pymongo
from pymongo import MongoClient
import sys, os
import base64
import json

BASE_PATH = os.path.abspath(__file__+ './')
sys.path.append(BASE_PATH)

app = Flask(__name__)

app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

# import views 
from inc.classes.views.users import UsersBp

# import consts
from inc.consts.consts import *

# import db
from inc.classes.db.Db import DbLib

# register views
app.register_blueprint(UsersBp)


@app.route('/')
def ping_server():
    response = Response(
        response= json.dumps({"API": "Desafio-Backend", "Version": 1.0}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
