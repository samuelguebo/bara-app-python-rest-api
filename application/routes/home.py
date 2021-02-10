import flask
from flask import Blueprint
from flask import Flask
import os
import re
import json

app = Flask(__name__)
home = Blueprint('home_bp', __name__)


@home.route('/')
def index():
    data = {"name" : "Jane"}
    return (data, 200)
