from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/<string:name>', methods = ['GET'])
def home(name):
    data = 'Hello ' + name + "! Welcome to my first API."
    return jsonify({'data':data})

@app.route('/convert/<int:temperature>', methods = ['GET'])
def convert(temperature):
    return jsonify({'data':(1.8*temperature+32)})

if __name__ == '__main__':
    app.run()