#random_walk.py
from random import choice


class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性，默认走5000步"""
        self.num_points = num_points
        # 所有随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿着这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

#rw_visual.py
import matplotlib.pyplot as plt
from chapter15.random_walk import RandomWalk

while True:
    # 创建一个RandWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    plt.plot(rw.x_values,rw.y_values) #模拟花粉在水滴表面的运动路径

    plt.show()

    keep_running=input("Make another walk?(y/n):")
    if keep_running=='n':
        break