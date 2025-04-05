import matplotlib.pyplot as plt

#BASIC STRUCTURE
# x = [2,5,3,6,4,7]
# plt.boxplot(x)
# plt.show()





#TO CHANGE THE SHAPE OF THE BOX AS NOTCH  (notch parameter)
# x = [2,5,3,6,4,7]
# plt.boxplot(x,notch=True)
# plt.show()





#TO CHANGE THE ORIENTATION OF THE BOX PLOT   (vert parameter)
# x = [2,5,3,6,4,7]
# plt.boxplot(x,notch=True,vert=False)
# plt.show()





#TO CHANGE THE WIDTH OF THE BOX
# x = [2,5,3,6,4,7]
# plt.boxplot(x,widths=0.6)
# plt.show()





#TO GIVE THE LABEL TO THE PLOT    (labels parameter)
# x = [2,5,3,6,4,7]
# plt.boxplot(x,labels=["python"])
# plt.show()





#TO FILL THE COLOR INSIDE THE BOX   (patch_artist parameter)
# x = [2,5,3,6,4,7]
# plt.boxplot(x,patch_artist=True)
# plt.show()





#TO SHOW OR INDICATE THE MEAN INSIDE THE BOX     (showmeans parameter)
# x = [2,5,3,6,4,7,120,150,115]
# plt.boxplot(x,showmeans=True)
# plt.show()





#TO EXTEND THE WHISK TO THE OUTLIER VALUE   (whis parameter)
      #(outlier is a point which shows the end point of the whisker when the data or values goes out of range)
# x = [2,50,3,6,4,7,120,150,115,200,350]
# plt.boxplot(x,showmeans=True,whis=2)        #you can try any value which join the outlier to the whisker
# plt.show()






#TO CHANGE THE COLOR AND SHAPE OF THE OUTLIER
# x = [2, 50, 3, 6, 4, 7, 120, 150, 115, 200, 350]
# # plt.boxplot(x,showmeans=True,sym="m")         #to change the color of outlier
# # plt.boxplot(x,showmeans=True,sym="+")       #to change the shape of outlier
# plt.boxplot(x,showmeans=True,sym="m*")      #to change the color and shape both of outlier
# plt.show()





#TO CHANGE THE COLOR OF THE BOX (OUTSIDE COLOR)    (boxprops parameter)
# x = [2, 50, 3, 6, 4, 7, 120, 150, 115, 200, 350]
# plt.boxplot(x,showmeans=True,sym="m",boxprops=dict(color="r"))
# plt.show()






#TO CHANGE THE COLOR OF THE CAP of whisk  (capprops parameter)
# x = [2, 50, 3, 6, 4, 7, 120, 150, 115]
# plt.boxplot(x,showmeans=True,sym="m",boxprops=dict(color="r"),capprops=dict(color="g"))
# plt.show()





#TO CHANGE THE COLOR OF THE WHISKER   (whiskprops parameter)
# x = [2, 50, 3, 6, 4, 7, 120, 150, 115]
# plt.boxplot(x,showmeans=True,sym="m",boxprops=dict(color="r"),whiskerprops=dict(color="violet"))
# plt.show()





#TO CHANGE THE COLOR OF THE MEDIAN LINE  (flierprops parameter)
# x = [2, 50, 3, 6, 4, 7, 120, 150, 115]
# plt.boxplot(x,showmeans=True,flierprops=dict(markeredgecolor="y"))
# plt.show()





#TO MAKE MULTIPLE BOX PLOTS
# x = [2, 50, 3, 6, 4, 7, 120, 150, 115]
# x1 = [20,55,44,22,3,7,77,33]
# y = [x,x1]
# plt.boxplot(y,labels=["python","c++"],showmeans=True,flierprops=dict(markeredgecolor="y"))
# plt.show()










































