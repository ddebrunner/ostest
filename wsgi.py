import os

for k in os.environ:
    print(k, os.environ[k])
    
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Dan!"

if __name__ == "__main__":
    application.run()

