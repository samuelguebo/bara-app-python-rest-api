from application.models.alchemy_encoder import AlchemyEncoder
import flask
from flask import Blueprint
from flask import Flask, jsonify
import os
import re
import json

app = Flask(__name__)
offer_bp = Blueprint('offer_bp', __name__)

@offer_bp.route('/')
def index():
    from application.dao.offer_dao import OfferDao
    from application import db
    
    result = [x.to_dict() for x in OfferDao(db).fetch(5)]
    data = result
    #data = jsonify(json.dumps(result, cls=AlchemyEncoder))
    return (jsonify(data), 200)
