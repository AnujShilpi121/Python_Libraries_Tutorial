import matplotlib.pyplot as plt

#BASIC SYNTAX
# x = [1,2,3,4,5,6]
# y = [1,2,3,4,5,6]
# plt.plot(x,y)
# plt.fill_between(x,y)
# plt.show()





#TO ADD XLABEL,YLABEL,TITLE,COLOR OF LINE
# x = [1,2,3,4,5,6]
# y = [1,2,3,4,5,6]
# plt.plot(x,y,color="r")
# plt.fill_between(x,y)
# plt.xlabel("x-axis----")
# plt.ylabel("y-axis----")
# plt.title("just for fun")
# plt.show()






#TO INCREASE THE WIDTH OF THE LINE
# x = [1,2,3,4,5,6]
# y = [1,2,3,4,5,6]
# plt.plot(x,y,color="r",linewidth=5)
# plt.fill_between(x,y)
# plt.xlabel("x-axis----")
# plt.ylabel("y-axis----")
# plt.title("just for fun")
# plt.show()




#TO SET AREA TO BE FILLED
# x = [1,2,3,4,5,6]
# y = [1,2,3,4,5,6]
# plt.plot(x,y,color="r",linewidth=5)
# plt.fill_between(x=[2,4],y1=3,y2=5)          #x=[start value,end value] ,y1 = start value , y2 = end value  (you can not pass y as a list)
# plt.xlabel("x-axis----")
# plt.ylabel("y-axis----")
# plt.title("just for fun")
# plt.show()






#TO CHANGE THE COLOR OF THE FILLED AREA
# x = [1,2,3,4,5,6]
# y = [1,2,3,4,5,6]
# plt.plot(x,y,color="r",linewidth=5)
# plt.fill_between(x=[2,4],y1=3,y2=5,color="y")          #x=[start value,end value] ,y1 = start value , y2 = end value  (you can not pass y as a list)
# plt.xlabel("x-axis----")
# plt.ylabel("y-axis----")
# plt.title("just for fun")
# plt.show()






#TO SET AREA TO BE FILLED VIA CONDITION (where parameter)     ----    values of x-axis and y-axis must be array because it is a numpy's method
# import numpy as np
# x = np.array([1,2,3,4,5,6])
# y = np.array([1,2,3,4,5,6])
# plt.plot(x,y,color="r",linewidth=5)
# plt.fill_between(x,y,color="yellow",where=(x>=2) & (x<=4))
# plt.xlabel("x-axis----")
# plt.ylabel("y-axis----")
# plt.title("just for fun")
# plt.show()




