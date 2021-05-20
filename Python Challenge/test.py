import unittest
import numpy as np
import json
from game import game


class TestGame(unittest.TestCase):


	def setUp(self):
		self.g = game()
		with open('config.json') as file:
			config = json.load(file)
		self.w = config['width']
		self.h = config['height']


	def test_window(self):
		np.testing.assert_array_equal(self.g.send_window(), np.zeros((self.w, self.h)))


	def test_pattern_adding(self):
		self.g.add_pattern(self.g.beehive, 0, 0)
		test_window = np.zeros((self.w, self.h))
		test_window[0:3, 0:4] = np.array([[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]])
		np.testing.assert_array_equal(self.g.send_window(), test_window)


	def test_beehive(self):
		self.g.add_pattern(self.g.beehive, 0, 0)
		self.g.update_window()
		test_window = np.zeros((self.w, self.h))
		test_window[0:3, 0:4] = np.array([[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]])
		np.testing.assert_array_equal(self.g.send_window(), test_window)
	

	def test_beacon(self):
		self.g.add_pattern(self.g.beacon, 0,5)
		self.g.update_window()
		test_window = np.zeros((self.w, self.h))
		test_window[0:4, 5:9] = np.array([[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]])
		np.testing.assert_almost_equal(self.g.send_window(), test_window, decimal=0)
	
	
if __name__ == '__main__':
	unittest.main()