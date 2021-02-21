from multiprocessing import Pool
class ThreadManager:

	def __init__(self, process_number, callback):
		"""
		Constructor of the ThreadManager class with its parameters

		:param process_number: Number of pool workers
		:param callback: function to be executed
		"""
		self.process_number = process_number
		self.callback = callback
		self.workers = []
		self.pool = None

	def create_pool(self):
		"""
		Create a pool of n work processes and 
		return the Pool object created
		"""
		self.pool = Pool(self.process_number)
		
		return self.pool

	def add_worker(self, worker):
		"""
		Add tasks to the pool of workers

		:param worker: long running task
		"""

		return self.workers.append(worker)

	def run(self):
		"""
		Trigger all the operations in the 
		thread pool
		"""
		with self.pool as p:
			p.map(self.callback, self.workers)
		
		return self.workers