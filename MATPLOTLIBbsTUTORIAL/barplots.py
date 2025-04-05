# import matplotlib.pyplot as plt
# import numpy as np
# x = ["Pyhton","c++","c","java"]
# y = [9,8,5,6]
# c = ["pink","g","y","b"]
# plt.xlabel("language",fontsize=15)
# plt.ylabel("numbers",fontsize=15)
# plt.title("Value Graph",fontsize=15)
# plt.bar(x,y)
# # plt.bar(x,y,width = 0.5,color = c,align = "edge")
# # plt.bar(x,y,width = 0.5,color = c,align = "center")
# # plt.bar(x,y,width = 0.5,color = c,align = "center",edgecolor = "skyblue")
# # plt.bar(x,y,width = 0.5,color = c,align = "center",edgecolor = "r",linewidth = 5)
# # plt.bar(x,y,width = 0.5,color = c,align = "center",edgecolor = "r",linewidth = 5,linestyle = ":")
# # plt.bar(x,y,width = 0.5,color = c,align = "center",edgecolor = "r",linewidth = 5,alpha = 0.6) #alpha = 0 to 1 float value
# #To add label to a graph
# plt.bar(x,y,width = 0.5,color = c,align = "center",edgecolor = "r",linewidth = 5,alpha = 0.6,label = "Bar graph")
# plt.legend()
# plt.show()







#TO MAKE MULTIPLE BAR GRAPH overlap
# import matplotlib.pyplot as plt
# x = ["Pyhton","c++","c","java"]
# y = [9,8,5,6]
# z = [4,5,3,2]
# # c = ["pink","g","y","b"]
# plt.xlabel("language",fontsize=15)
# plt.ylabel("numbers",fontsize=15)
# plt.title("Value Graph",fontsize=15)
# plt.bar(x,y,width = 0.5,color = "r",label = "popularity1")
# plt.bar(x,z,width = 0.5,color = "y",label = "populatity2")
# plt.legend()
# plt.show()






#TO MAKE MULTIPLE BAR GRAPH  WITHOUT OVERLAPING
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = ["Pyhton","c++","c","java"]
# y = [9,8,5,6]
# z = [4,5,3,2]
#
# width = 0.2
# p = np.arange(len(x))
# p1 = [j+width for j in p]
#
# plt.xlabel("language",fontsize=15)
# plt.ylabel("numbers",fontsize=15)
# plt.title("Value Graph",fontsize=15)
#
# plt.bar(p,y,width,color = "r",label = "popularity1")
# plt.bar(p1,z,width,color = "y",label = "populatity2")
# plt.xticks(p+width/2,x)           #it is used for replacing x-axis ticks
# plt.yticks(rotation = 40)
# plt.legend(loc = 1)        #quadrant 1   (by default it adjust itself in blank space)
# plt.show()




#TO MAKE HORIZONTAL BAR GRAPH
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = ["Pyhton","c++","c","java"]
# y = [9,8,5,6]
# z = [4,5,3,2]
#
# width = 0.2
# p = np.arange(len(x))
# p1 = [j+width for j in p]
#
# plt.xlabel("language",fontsize=15)
# plt.ylabel("numbers",fontsize=15)
# plt.title("Value Graph",fontsize=15)
#
# plt.barh(p,y,width,color = "r",label = "popularity1")
# plt.barh(p1,z,width,color = "y",label = "populatity2")
# plt.xticks(p+width/2,x,rotation = 40)
# plt.yticks(y,rotation = 40)
# plt.legend()
# plt.show()

