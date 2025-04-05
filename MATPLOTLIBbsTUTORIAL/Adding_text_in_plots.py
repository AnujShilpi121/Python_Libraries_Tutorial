import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [10,12,3,4,5,6]
plt.plot(x,y)

                #ADDING TEXT IN PLOT AT A SPECIFIC POSITION
# plt.text(2,12,"Python",style="italic",bbox=dict(facecolor="r",edgecolor="yellow",linewidth=1))
# plt.text(1,10,"C++",style="italic",bbox=dict(facecolor="r",edgecolor="yellow",linewidth=1))


                 #ADDING ARROWS ,POINTING AT A SPECIFIC POINT
# plt.annotate("python",xy=(4,3),xytext=(3.5,11),arrowprops=dict(facecolor="black",shrink=True))    #you can pass integer value also in shrink

                #ADDING LEGEND LABEL
# plt.legend(["Linear_plot"],loc=9,facecolor="red",edgecolor="y",shadow=True,framealpha=0.5)
# plt.show()