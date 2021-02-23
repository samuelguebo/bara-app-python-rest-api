from config import executor
class ThreadManager:

	def __init__(self):
		"""
		Constructor of the ThreadManager class with its parameters

		:param process_number: Number of pool workers
		:param callback: function to be executed
		"""
		self.executor = executor
		self.workers = []


	def add_worker(self, worker, params):
		"""
		Add tasks to the pool of workers

		:param worker: a tuple containing
			long running task and its 
			parameter
		"""

		return self.workers.append((worker, params))

	def run(self):
		"""
		Trigger all the operations in the 
		thread pool
		"""
		for callback, params in self.workers: 
			self.executor.submit(callback, params)
			
		return self.workers