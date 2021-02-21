from application.services.log_manager import LogManager
from application.services.thread_manager import ThreadManager
from time import time
from datetime import datetime
import timeago

class CronManager():
	"""
	Helper class for triggering cron operations. It avoids 
	unecessary cron tasks by relying on a log file,
	a sort of cache, which contains ID and timestamp
	of recently run cron operations.
	"""

	def __init__(self):
		"""
		Default constructor which will initiate
		some varibales and make them available
		to the class methods.
		"""
		self.tasks = []
		self.log_manager = LogManager()
		self.log = self.log_manager.get_cron_log()


	def get_latest_cron(self, cron):
		""" 
		Get the timestamp of the latest cron operation
		which was ran for a specific Cron object.
		"""
		
		return self.log_manager.get_entry(cron.ID)

	def add(self, cron):
		"""
		Build and array of cron operations

		:param cron: a Cron object or of its children
		"""
		
		self.tasks.append(cron)

	def execute(self):
		"""
		Process all cron operations in a 
		sequential batch asyncronously
		"""
		thread_manager = ThreadManager(4, self.run_async)
		thread_manager.create_pool()
		
		for cron in self.tasks:
			if not self.has_cache(cron):
				thread_manager.add_worker(cron)
		
		if len(thread_manager.workers) > 1:
			thread_manager.run()

	def run_async(self, cron):
		"""
		Helper function to be used
		with ThreadManager
		"""
		self.log_manager.generate_log(cron.ID)
		cron.run()

	def has_cache(self, cron):
		""" 
		Process the Cron task if the time lapse since the latest 
		operation exceed the cache_delay

		:param cache_delay: Time lapse since last run in hours
		:param cron: Cron object or child
		"""
		if cron.ID not in self.log:
			self.log_manager.generate_log(cron.ID)
			return False

		latest_time_stamp = datetime.fromtimestamp(self.get_latest_cron(cron))
		now = datetime.fromtimestamp(time())

		# Difference in hours
		lapsed_time = (now - latest_time_stamp).seconds / 3600
		
		# Check whether last cron operation was run recently
		if cron.CACHE_DELAY > lapsed_time:
			return True
	
	def get_logs(self):
		return ['{} was updated {}.'.format(cron.ID, timeago.format(
			self.get_latest_cron(cron))) for cron in self.tasks]

	def reset(self):
		"""
		Reset tasks list
		"""
		self.tasks = []