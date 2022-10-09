from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/<string:name>', methods = ['GET'])
def home(name):
    data = 'Hello ' + name + "! Welcome to my first API."
    return jsonify({'data':data})

@app.route('/convert/<int:temperature>', methods = ['GET'])
def convert(temperature):
    return jsonify({'data':(1.8*temperature+32)})

if __name__ == '__main__':
    app.run(debug = True)