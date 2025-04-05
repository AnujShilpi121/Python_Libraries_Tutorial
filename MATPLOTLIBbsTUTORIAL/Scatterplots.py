import matplotlib.pyplot as plt
# x = [1,2,3,4,5,6]
# y = [7,8,9,4,5,6]
#
# plt.xlabel("numbers",fontsize = 14)
# plt.ylabel("numbers",fontsize = 14)
# plt.title("scatter plot",fontsize = 16)
#
# # plt.scatter(x,y)
# plt.scatter(x,y,color = "r")
# plt.show()






#ADDING DIFFERENT COLORS TO THE SCATTER GRAPH
# x = [1,2,3,4,5,6]
# y = [7,8,9,4,5,6]
# c = ["r","b","g","y","brown","skyblue"]
#
# plt.xlabel("numbers",fontsize = 14)
# plt.ylabel("numbers",fontsize = 14)
# plt.title("scatter plot",fontsize = 16)
#
# plt.scatter(x,y,color = c)
# plt.show()






#TO INCREASE THE SIZE OF THE SCATTER
# x = [1,2,3,4,5,6]
# y = [7,8,9,4,5,6]
# c = ["r","b","g","y","brown","skyblue"]
# sizes = [50,1000,60,200,80,90]
#
# plt.xlabel("numbers",fontsize = 14)
# plt.ylabel("numbers",fontsize = 14)
# plt.title("scatter plot",fontsize = 16)
#
# plt.scatter(x,y,color = c,s = sizes)
# plt.show()







#TO REDUCE TRANSPARENCY OF THE SCATTER
# x = [1,2,3,4,5,6]
# y = [7,8,9,4,5,6]
# c = ["r","b","g","y","brown","skyblue"]
# size = [50,1000,60,200,80,90]
#
# plt.xlabel("numbers",fontsize = 14)
# plt.ylabel("numbers",fontsize = 14)
# plt.title("scatter plot",fontsize = 16)
#
# plt.scatter(x,y,color = c,s = size,alpha=0.4)   #alpha should be in between 0 to 1
# plt.show()







#TO CHANGE THE SHAPE OF SCATTERS OR MARKER OF SCATTERS
# x = [1,2,3,4,5,6]
# y = [7,8,9,4,5,6]
# c = ["r","b","g","y","brown","skyblue"]
# size = [50,1000,60,200,80,90]
#
# plt.xlabel("numbers",fontsize = 14)
# plt.ylabel("numbers",fontsize = 14)
# plt.title("scatter plot",fontsize = 16)
#
# plt.scatter(x,y,color = c,s = size,marker = "*",edgecolor="black",linewidth = 2)
# plt.show()







# FILLING COLOR IN SCATTER USING CMAP FUNCTION PARAMETER
# x = [1,2,3,4,5,6]
# y = [7,8,9,4,5,6]
# c = [100,50,40,90,60,50]           #colour range should between 0 - 100  in case of cmap parameter
# size = [50,1000,60,200,80,90]
#
# plt.xlabel("numbers",fontsize = 14)
# plt.ylabel("numbers",fontsize = 14)
# plt.title("scatter plot",fontsize = 16)
#
# # plt.scatter(x,y,c = c,s = size,cmap = "viridis")
# plt.scatter(x,y,c = c,s = size,cmap = "BrBG")
#
#         #to add colorbar
#
# t = plt.colorbar()
# t.set_label("COLOR BAR",fontsize = 16)
# plt.show()







# #TO PLOT MULTIPLE SCATTER PLOTS IN A SINGLE GRAPH
# x = [1,2,3,4,5,6]
# y = [7,8,9,4,5,6]
# z = [1,3,5,7,9,11]
# c = [100,50,40,90,60,50]
# size = [50,1000,60,200,80,90]
#
# plt.xlabel("numbers",fontsize = 14)
# plt.ylabel("numbers",fontsize = 14)
# plt.title("scatter plot",fontsize = 16)
#
# # plt.scatter(x,y,c = c,s = size,cmap = "viridis")
# plt.scatter(x,y,c = c,s = size,cmap = "BrBG")
# plt.scatter(x,z,c = c,s = size,cmap = "BrBG")
# #to add colorbar
# t = plt.colorbar()
# t.set_label("COLOR BAR",fontsize = 16)
# plt.show()








