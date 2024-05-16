#import flask
from flask import Flask
import pymongo

#create app object
app = Flask(__name__)

#define the hello function with route decorator
@app.route("/")
def hello():
    return '<h1>Hello Lindy</h1>'

@app.route('/aaron')
def aaron():
    return '<h1>Aaron loves Lindy a whole lot!</h1>'