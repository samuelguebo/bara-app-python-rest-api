from flask import Flask
from flask import Blueprint, jsonify
test_bp = Blueprint('test_bp', __name__)

@test_bp.route('/test')
def index():
    
    # Models should be imported after the app is created
    from .. import db
    from ..models.offer import Offer
    from ..models.user import User

    offer = Offer('http://ddd.com', 'Joh', 'Lorem ipsum', '12/07/2020','19/08/2020')
    admin = User('admin', 'admin@example.com')

    db.create_all() # In case user table doesn't exists already. Else remove it.    
    db.session.add(admin)
    db.session.add(offer)
    db.session.commit() # This is needed to write the changes to database

    results = Offer.query.all()

    print(results)

    return ({'hello': 'go'}, 200)
