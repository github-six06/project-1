import matplotlib.pyplot as plt
from die import Die
die_1 = Die()
die_2 = Die()

#创立2个D6
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析分别出现几次
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result+1):
    frequecy = results.count(value)
    frequencies.append(frequecy)

x_values = list(range(1,max_result+1))
y_values = frequencies
# 设置绘图窗口的尺寸
plt.figure(figsize=(20, 12))
plt.scatter(x_values,y_values, s=15)
plt.show()
