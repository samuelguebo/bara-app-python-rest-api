import flask
from flask import Blueprint
from flask import Flask
import os
import re
import json

app = Flask(__name__)
home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/')
def index():
    data = {"name" : "Home"}
    return (data, 200)
