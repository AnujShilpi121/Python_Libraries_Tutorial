import matplotlib.pyplot as plt

#BASIC SYNTAX
# x = [1,2,3,5,4,6]
# y = [1,12,32,52,4,6]
# plt.stackplot(x,y)
# plt.show()





#TO PLOT MULTIPLE STACK PLOT OR AREA PLOT
# x = [1,2,3,5,4,6]
# y1 = [1,12,3,5,4,6]
# y2 = [1,12,2,2,4,6]
# y3 = [1,12,32,52,4,6]
# plt.stackplot(x,y1,y2,y3)
# plt.show()






#TO ADD LEGEND LABEL
# x = [1,2,3,5,4,6]
# y1 = [1,12,3,5,4,6]
# y2 = [1,12,2,2,4,6]
# y3 = [1,12,32,52,4,6]
#
# l = ["python","c++","java"]      #adding labels
# plt.stackplot(x,y1,y2,y3,labels=l)
# plt.legend(loc=2)                #label will show in the second quadrant
# plt.show()






#TO CHANGE THE COLOR OF THE AREA
# x = [1,2,3,5,4,6]
# y1 = [1,12,3,5,4,6]
# y2 = [1,12,2,2,4,6]
# y3 = [1,12,32,52,4,6]
# l = ["python","c++","java"]
# plt.stackplot(x,y1,y2,y3,labels=l,colors=["m","y","r"])
# plt.legend(loc=2)
# plt.show()







#TO CHANGE THE VALUE OF THE BASELINE (baseline parameter)
# x = [1,2,3,5,4,6]
# y1 = [1,12,3,5,4,6]
# y2 = [1,12,2,2,4,6]
# y3 = [1,12,32,52,4,6]
# l = ["python","c++","java"]
#
# # plt.stackplot(x,y1,y2,y3,labels=l,colors=["m","y","r"],baseline="sym")
# # plt.stackplot(x,y1,y2,y3,labels=l,colors=["m","y","r"],baseline="wiggle")
# plt.stackplot(x,y1,y2,y3,labels=l,colors=["m","y","r"],baseline="zero")
#
# plt.legend(loc=2)
# plt.show()







#TO ADD XLABEL,YLABEL,TITLE
# x = [1,2,3,5,4,6]
# y1 = [1,12,3,5,4,6]
# y2 = [1,12,2,2,4,6]
# y3 = [1,12,32,52,4,6]
# l = ["python","c++","java"]
# plt.stackplot(x,y1,y2,y3,labels=l,colors=["m","y","r"])
# plt.xlabel("Languages value")
# plt.ylabel("Languages Area")
# plt.title("Area Plot")
# plt.legend(loc=2)
# plt.show()

























