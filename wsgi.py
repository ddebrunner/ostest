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
    #x = requests.get('https://external-postman-echo.myproject.svc/get?foo1=bar1&foo2=bar2')
    return jsonify(x.json())

@application.route("/strms")
def strms():
    x = requests.get('http://dan-nginx-tonic.myproject.svc:8080/streams/rest/instances', auth=(os.environ['DAN_STRMS_USER'],os.environ['DAN_STRMS_PWD']))
    return jsonify(x.json())

if __name__ == "__main__":
    application.run()

