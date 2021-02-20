
import matplotlib.pyplot as plt
 x_values  = [1,2,3,4,5]
y_values = [1,8,27,64,125]
plt.title("Li Fang ")
plt.plot(x_values,y_values,linewidth = 5)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis = 'both' , labelsize = 14)
plt.show()


import matplotlib.pyplot as plt
x_values  = list(range(1,50001))
y_values = [x**3 for x in x_values]
plt.title("Li Fang ")
plt.scatter(x_values,y_values,linewidth = 5,edgecolor = 'none')
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis = 'both' , labelsize = 14)
plt.show()




