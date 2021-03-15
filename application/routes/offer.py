from flask import Blueprint
from flask import Flask, jsonify
from config import db
from application.dao.offer_dao import OfferDao
from application.models.offer import Offer
from application.models.offer import OfferSchema
from application.models.offer import TagsSchema

offer_bp = Blueprint('offer_bp', __name__)


@offer_bp.route('/')
def index():

    offer_schema = OfferSchema(many=True)
    data = offer_schema.dump(OfferDao().fetch(30))

    return jsonify(data)


@offer_bp.route('/tags')
def tags():

    tag_schema = TagsSchema(many=True)
    data = tag_schema.dump(OfferDao().get_tags())

    return jsonify(data)


@offer_bp.route('/tags/<title>')
def find_by_tag(title):

    offer_schema = OfferSchema(many=True)
    data = offer_schema.dump(OfferDao().find_by_tag(title))
    return jsonify(data)
