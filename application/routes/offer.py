from flask import Blueprint
from flask import Flask, jsonify
from config import db
from application.dao.offer_dao import OfferDao
from application.models.offer import Offer
from application.models.offer import OfferSchema

app = Flask(__name__)
offer_bp = Blueprint('offer_bp', __name__)


@offer_bp.route('/')
def index():
    
    offer_schema = OfferSchema(many=True) 
    data = offer_schema.dump(Offer.query.limit(5))
    
    return (jsonify(data), 200)
