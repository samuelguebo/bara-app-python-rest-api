import pytest
import json
from application import create_app

"""
Test suite for the routes related to the default
page and its relevant endpoints.    
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

def test_home_route(client):
	"""
	Testing the route /
	"""
	resp = client.get('/')
	data = json.loads(resp.data)
	
	assert 'name' in data 
