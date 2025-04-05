import matplotlib.pyplot as plt

# x = [10,20,30,40]
#  #to add labels of each element
# y = ["c","c++","java","python"]
# plt.pie(x,labels = y)
# plt.show()




#TO SPLIT ONE PART OF PIE TO SHOW IT DIFFERENT

# x = [10,60,30,40]
      #to add labels of each element
# y = ["c","c++","java","python"]
     #to explode or split
# ex = [0.4,0.0,0.0,0.0]
# plt.pie(x,labels = y,explode=ex)
# plt.show()






#TO ADD COLORS

# x = [10,60,30,40]
      #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c)
# plt.show()







#TO ADD PERCENTAGE AT EACH PIE   [parameter ---- autopct = "%string%%"]

# x = [10,60,30,40]
#  #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# # plt.pie(x,labels = y,explode=ex,colors=c,autopct="%i%%")
# # plt.pie(x,labels = y,explode=ex,colors=c,autopct="%f%%")
# # plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.1f%%")
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%.2f%%")
# plt.show()








#SHADOW PARAMATER - To show shadow of each pie
# x = [10,60,30,40]
   #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True)
# plt.show()







#TO INCREASE or DECREASE RADIUS OF A PIE CHART
# x = [10,60,30,40]
#  #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,radius=1.5)
# plt.show()







#TO ADJUST LABEL DISTANCE    (parameter - labeldistance)
# x = [10,60,30,40]
#  #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",labeldistance=1.1)
# plt.show()







#TO ROTATE CIRCLE OR TO SET START ANGLE      (parameter - startangle)
# x = [10,60,30,40]
#  #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,startangle=90)
# plt.show()







#TO INCREASE THE FONTSIZE
# x = [10,60,30,40]
#  #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,textprops={"fontsize":15})
# plt.show()








#COUNTERCLOCK - to rotate each pie in clockwise or anticlockwise
# x = [10,60,30,40]
#          #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# # plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,counterclock=True)   #anti clockwise by default
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,counterclock=False)   #clockwise
# plt.show()








#TO INCREASE THE SHADOW OR LINEWIDTH
# x = [10,60,30,40]
#          #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,counterclock=False,wedgeprops={"linewidth":6})
# plt.show()







#TO INCREASE THE WIDTH OF EACH PIE
# x = [10,60,30,40]
#          #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,counterclock=False,wedgeprops={"linewidth":6,"width":0.5})
# plt.show()









#TO CHANGE THE EDGECOLOR OF CHART
# x = [10,60,30,40]
#          #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,counterclock=False,wedgeprops={"linewidth":4,"width":0.5,"edgecolor":"m"})
# plt.show()







#TO CHANGE THE CENTER OF THE CHART
# x = [10,60,30,40]
#          #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,counterclock=False,center=(3,3))
# plt.show()







#TO ROTATE THE LABEL OF THE CHART
# x = [10,60,30,40]
#          #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,counterclock=False,
#         wedgeprops={"linewidth":4,"width":0.5,"edgecolor":"m"},rotatelabels=True)
# plt.show()









#TO MAKE THE LEGEND LABEL
# x = [10,60,30,40]
#          #to add labels of each element
# y = ["c","c++","java","python"]
# ex = [0.4,0.0,0.0,0.1]
# c = ["red","g","y","blue"]
# plt.pie(x,labels = y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,counterclock=False,
#         wedgeprops={"linewidth":4,"width":0.5,"edgecolor":"m"})
# plt.title("Programming Languages")
# plt.legend()
# plt.legend(loc=4)     #alse you can give the location of the legend label as quadrant
# plt.show()







#TO MAKE DOT PIE CHART OR WITHOUT PARTITION CHART
# plt.pie([1])
# plt.show()






#TO MERGE TO PIE CHART OR TO MAKE PIE CHART INSIDE A ANOTHER PIE CHART
# x = [10,20,30,40]
# x1 = [20,50,10,30]
#    #to add labels of each element
# y = ["c","c++","java","python"]
# plt.pie(x,labels = y,radius=1.5)
# plt.pie(x1,labels = y,radius=0.5,colors=["r","g","m","y"])
# plt.show()







#TO MAKE HOLLOW PIE CHART

# x = [10,20,30,40]
# x1 = [1]
#    #to add labels of each element
# y = ["c","c++","java","python"]
# plt.pie(x,labels = y,radius=1.5)
# plt.pie(x1,colors="w",radius=0.8)
# plt.show()

                #another way
# x = [10,20,30,40]
#    #to add labels of each element
# y = ["c","c++","java","python"]
# plt.pie(x,labels = y,wedgeprops={"width":0.5})
# plt.show()

              #another way
# x = [10,20,30,40]
#    #to add labels of each element
# y = ["c","c++","java","python"]
# plt.pie(x,labels = y)
# c = plt.Circle(xy=(0,0),radius=0.5,facecolor="w")
# plt.gca().add_artist(c)
# plt.show()







































