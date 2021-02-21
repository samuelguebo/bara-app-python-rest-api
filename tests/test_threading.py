from multiprocessing import Pool
from application.services.thread_manager import ThreadManager
class TestThreading:
	"""
	Test suite for running parallel operations
	through threading.
	"""

	def long_running_task(self, task):
		print('type of task is: {}'.format(type(task)))

	def test_create_pool(self):
		# Create a pool of work process
		pool = ThreadManager(5, self.long_running_task).create_pool()
		assert 'Pool' in str(type(pool))

	def test_add_worker(self):
		thread_manager = ThreadManager(4, self.long_running_task)
		thread_manager.create_pool()
		thread_manager.add_worker('maria')
		
		workers = thread_manager.workers
		assert len(workers) == 1


	def test_run_pool(self):
		thread_manager = ThreadManager(4, self.long_running_task)
		thread_manager.create_pool()
		thread_manager.add_worker('Maria')
		thread_manager.add_worker('Ines')
		thread_manager.add_worker('Valence')
		
		assert len(thread_manager.run()) == 3
		