import matplotlib.pyplot as plt

x_vaules = list(range(1,5000))
y_values = [x*x*x for x in x_vaules]
plt.scatter(x_vaules,y_values,edgecolors='none',s = 40)
#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
#设置刻度数值的大小
plt.tick_params(axis = 'both',labelsize = 14)
plt.show()




