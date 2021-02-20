import pygal
from die import Die
die_1 = Die(8)
die_2 = Die(8)
#创立2个D6
results = []

for roll_num in range(10000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析分别出现几次1-6
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequecy = results.count(value)
    frequencies.append(frequecy)

#对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling two D8 dice 10000 times.'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8+D8',frequencies)
hist.render_to_file('15.7.svg')

