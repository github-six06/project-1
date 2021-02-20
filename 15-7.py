from random import randint
class Die(object):
	"""docstring for Die"""
	def __init__(self, num_sides = 8):
		self.num_sides = num_sides
 
	def roll(self):
		return randint(1,self.num_sides)
from die import Die
import pygal
die1 = Die()
die2 = Die()
results = []
for roll_num in range(1000):
	result = die1.roll() + die2.roll()
	results.append(result)
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
hist = pygal.Bar()
hist.title = "Result of rolling me D8 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
 
hist.add('D8+D8',frequencies)
hist.render_to_file('dice1_visual.svg')
