
import matplotlib.pyplot as plt
from die import Die
 
die1 = Die()
die2 = Die()
results = []
 
for roll_num in range(1000):
	result = die1.roll() + die2.roll()
	results.append(result)
# print(results)
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(1,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)
plt.plot(list(range(1,max_result+1)),frequencies,linewidth = 2)
plt.title("Result of rolling me D6 1000 times.")
plt.xlabel ("Result",fontsize = 14)
plt.ylabel("Square of D6 1000 times")
plt.show()
