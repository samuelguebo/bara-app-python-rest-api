from flask import Flask
from flask_executor import Executor
from application.services.educarriere_cron import EducarriereCron
from application.services.thread_manager import ThreadManager
import requests
import json

class TestThreading:
	"""
	Test suite for running parallel operations
	through threading.
	"""
	
	app = Flask(__name__)
	# executor = Executor(app)
	executor = ThreadManager()
	
	def long_running_task(self, task='Maria'):
		content = requests.get('https://jsonplaceholder.typicode.com/todos/1').text
		print('data is: {}'.format(json.loads(content)))
		EducarriereCron().run()

	def test_run_pool(self):
		with self.app.test_request_context():
			self.executor.add_worker(self.long_running_task)
			self.executor.run()

    	