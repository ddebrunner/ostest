import os
import requests




for k in os.environ:
    print(k, os.environ[k])
    
from flask import Flask, jsonify
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Dan!"

@application.route("/pme")
def pme():
    x = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2')
    return jsonify(x.json())

if __name__ == "__main__":
    application.run()

