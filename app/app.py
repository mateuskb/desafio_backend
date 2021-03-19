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

@app.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = DbLib().connect(db="desafio")
        
        _users = db.users.find()

        users = [{
            "Nome": user["nome"],
            "CPF": user["cpf"], 
            "celular": user["celular"], 
            "score": user["score"], 
            "negativado": user["negativado"]
        } for user in _users]

        response = Response(
            response= json.dumps({"users": users}),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        response = Response(
            response= json.dumps({"ok": False}),
            status=500,
            mimetype='application/json'
        )
        return response
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
