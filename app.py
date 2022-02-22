#import dependencies
from flask import Flask

#Create the app
app = Flask(__name__)

#Create flask routes
#first define the starting point, aka root
@app.route('/')
def hello_world():
    return "Hello world"

