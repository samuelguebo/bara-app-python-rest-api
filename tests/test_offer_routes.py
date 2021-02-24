import pytest
import json
from application import create_app


"""
Test suite for the routes related to the
Offer models and its relevant endpoints.    
"""

@pytest.fixture
def client():
	app = create_app()
	testing_client = app.test_client()

	# Establish an application context before running the tests.
	ctx = app.app_context()
	ctx.push()

	yield testing_client  # this is where the testing happens!

	ctx.pop()

def test_offer_list_route(client):
	"""
	Testing the route /offer
	"""
	resp = client.get('/offer/')
	data = json.loads(resp.data)[0]
	
	assert 'content' in data 

def test_cron_route(client):
	"""
	Testing the route /
	"""
	resp = client.get('/cron/')
	data = json.loads(resp.data)[0]
	
	assert len(data) > 0
		