import matplotlib.pyplot as plt
x_values  = [1,2,3,4,5]
y_values = [1,8,27,64,125]
plt.title("Li Fang ")
plt.plot(x_values,y_values,linewidth = 5,c = 'red')
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis = 'both' , labelsize = 14)
plt.show()
