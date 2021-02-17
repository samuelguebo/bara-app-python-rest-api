import flask
from flask import Blueprint
from flask import Flask, send_from_directory
from config import Config
import os
import re
import json

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def index():
    data = {"name" : "Home"}
    return (data, 200)

@home_bp.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

