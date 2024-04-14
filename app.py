import json
from flask import Flask, jsonify, request
from src.endpoints import algo_blueprint

app = Flask(__name__)
app.register_blueprint(algo_blueprint)

if __name__ == '__main__':
   app.run(port=5000)