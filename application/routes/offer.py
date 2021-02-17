from flask import Blueprint
from flask import Flask, jsonify
from config import db
from application.dao.offer_dao import OfferDao
from application.models.offer import Offer
from application.models.offer import OfferSchema

offer_bp = Blueprint('offer_bp', __name__)

@offer_bp.route('/')
def index():
    
    offer_schema = OfferSchema(many=True) 
    data = offer_schema.dump(Offer.query.limit(30))
    
    return (jsonify(data), 200)
