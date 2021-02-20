from die import Die
import pygal
 
die1 = Die()
die2 = Die()
die3 = Die()
results = []
 
for roll_num in range(1000):
	result = die1.roll() + die2.roll() +  die3.roll()
	results.append(result)
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(2,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
 
hist = pygal.Bar()
hist.title = "Result of rolling me D6 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
 
hist.add('D6+D6+D6',frequencies)
hist.render_to_file('dice1_visual.svg')
