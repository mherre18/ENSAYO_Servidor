from flask import Flask
from flask import request
from flask import jsonify
from time import sleep

app = Flask(__name__)

baseBicis = {
    '01': {
        "Voltage" : 25,
        "Conector" : '1A'
    },
    '02' : {
        "Voltage" : 36,
        "Conector" : '1B'
    },
    '03': {
        "Voltage" : 48,
        "Conector" : '1A'
    },
    '04' : {
        "Voltage" : 25,
        "Conector" : '1B'
    },
    '05' : {
        "Voltage" : 36,
        "Conector" : '1A'
    }
}

dbUsers = {
    '32018083': {
        'Type' : 02,
        'Charge' : 'lectura_sensor',
        'State' : 'lectura_qr'
    },
    '10284174':{
        'Type' : 05,
        'Charge' : 'lectura_sensor',
        'State' : 'lectura_qr'
    },
    '17345126':{
        'Type' : 01,
        'Charge' : 'lectura_sensor',
        'State' : 'lectura_qr'
    }
}

@app.route("/bases")
def bases():
    return "Bienvenido su Info Bici"

@app.route("/bases/bicis", methods=["GET"])
def getBicis():
    if request.method == 'GET':
        return jsonify(baseBicis)

@app.route("/bases/bicis/<id>", methods = ["GET"])
def getById(id):
    if request.method == 'GET':
        return jsonify(baseBicis[id])

@app.route("/users/<id>", methods = ["GET"])
def getUsers(id):
    if request.method == 'GET':
        return jsonify(dbUsers[id])

@app.route("/users", methods=["GET"])
def getUser():
    if request.method == 'GET':
        return jsonify(dbUsers)        

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
