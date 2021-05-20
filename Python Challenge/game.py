#!/usr/bin/env python3


"""
__author__ = Arkajyoti Basak
__email__ = abasak_be18@thapar.edu
Conway's Game of Life
"""


import numpy as np
import time
import json 


class game():

	# patterns
	random  = np.random.choice(2, (30, 30), p=[0.3, 0.7])
	beehive = np.array([[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]])
	beacon  = np.array([[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]])
	glider  = np.array([[0, 0, 1], [1, 0, 1], [0, 1, 1]])
	LWSS    = np.array([[0, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]])

	glidergun = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);



	def __init__(self):

		# load configurations from json
		with open('config.json') as file:
			config = json.load(file)

		self.width = config["width"]
		self.height = config["height"]
		self.time_delay = config["time_delay"]
		self.window = np.random.randint(0,1, size=(self.width, self.height))
		self.counter = 1



	def add_pattern(self, pattern, x, y):
		"""
		add pattern inside the matrix at position (x,y)
		"""

		w, h = pattern.shape
		x = np.clip(x, 0, self.width - x -1)
		y = np.clip(y, 0, self.height - y -1 )
		self.window[x:x+w, y:y+h] = pattern



	def count_neighbours(self, x, y): 
		"""
		returns the sum of lives around the cell at horizontal, vertical and diagonal directions
		"""

		return int(self.window[(x-1)  % self.width, (y-1) % self.height] + 
					self.window[(x-1) % self.width, (y)   % self.height] + 
					self.window[(x-1) % self.width, (y+1) % self.height] +
					self.window[(x)   % self.width, (y-1) % self.height] + 
					self.window[(x)   % self.width, (y+1) % self.height] +
					self.window[(x+1) % self.width, (y-1) % self.height] + 
					self.window[(x+1) % self.width, (y)   % self.height] + 
					self.window[(x+1) % self.width, (y+1) % self.height])
				    


	def update_window(self):

		_window = self.window.copy()
		i,j = self.window.shape
		for x in range(i):
			for y in range(j):
				count = self.count_neighbours(x, y)
				if self.window[x,y] == 1:
					if count<2 or count>3:
						_window[x,y] = 0
				else:
					if count == 3:
						_window[x,y] = 1

		self.window = _window
		self.counter += 1



	def convert_to_char(self, x):
		return "*" if x == 1 else " "



	def display(self):
		for row in self.window:
			print(" ".join(map(self.convert_to_char, row)))



	def move_cursor_up(self):
		print("\033[%dA" % (self.height+2))
	  


	def move_cursor_down(self):
		print("\033[%dB" % (self.height+2))



	def main(self):
		print("["+str(self.counter)+"]")
		self.display()
		self.move_cursor_up()
		self.update_window()
		time.sleep(self.time_delay)



	def send_window(self):
		return self.window
	
