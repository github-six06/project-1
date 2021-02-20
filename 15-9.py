
#15-9
import pygal
from chapter15.die import Die

die1=Die()
die2=Die()

results=[die1.roll()*die2.roll() for roll_num in range(50000)]

#分析结果
max_result=die1.num_sides*die2.num_sides
frequences = [results.count(value) for value in range(1,max_result+1)]

#对结果进行可视化
hist = pygal.Bar()
hist.title="Results of rolling three D6 50000 times."
hist.x_labels=list(range(1,37))
hist.x_title="Result"
hist._y_title="Frequence of Result"

hist.add('D6*D6',frequences)
hist.render_to_file('multip_visual.svg')