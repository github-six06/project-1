#15-8
die.py
from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
three dice.py
import pygal
from chapter15.die import Die

die1=Die()
die2=Die()
die3=Die()

results=[die1.roll()+die2.roll()+die3.roll() for roll_num in range(50000)]

#分析结果
max_result=die1.num_sides+die2.num_sides+die3.num_sides
frequences = [results.count(value) for value in range(3,max_result+1)]

#对结果进行可视化
hist = pygal.Bar()
hist.title="Results of rolling three D6 50000 times."
hist.x_labels=list(range(3,19))
hist.x_title="Result"
hist._y_title="Frequence of Result"

hist.add('D6+D6+D6',frequences)
hist.render_to_file('three_visual.svg')