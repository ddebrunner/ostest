import os
import requests




for k in os.environ:
    print(k, os.environ[k])
    
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Dan!"

@application.roubt("/pme")
def pme():
    x = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2')
    return x.json()

if __name__ == "__main__":
    application.run()

