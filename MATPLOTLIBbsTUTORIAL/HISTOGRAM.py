import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(10,60,50)
n = []
     #To seperate with comma
for element in x:
    n.append(element)
print(n)



#BASIC SYNTAX

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2)
# plt.show()






# #ADDING BINS        ----     Bins are nothing but the tower or bar printed in range like 10-20

# l = [10,20,30,40,50,60]
# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")

# plt.hist(n,color="g",edgecolor="r",linewidth=2,bins=l)

        #data distributed in 6 bins
# plt.hist(n,color="g",edgecolor="r",linewidth=2,bins=6)
       #auto bins
# plt.hist(n,color="g",edgecolor="r",linewidth=2,bins="auto")
       #giving range to each bins
# plt.show()






# #ADDING RANGE OF DATA  (extending x-axis)

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,bins="auto",range=(0,200))
# plt.show()






#COMMULATIVE PARAMETER - data will be represented in comulative frequency order

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,cumulative=1)
# plt.hist(n,color="g",edgecolor="r",linewidth=2,cumulative=-1)
# plt.show()






# #MERGING TWO COMULATIVE FREQUENCY DATA
# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,cumulative=1)
# plt.hist(n,color="b",edgecolor="r",linewidth=2,cumulative=-1)
# plt.show()





# #BOTTOM PARAMETER

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,bottom=10)
# plt.show()





# #ALIGN (left,right,mid)

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,align="mid")           #by default
# # plt.hist(n,color="g",edgecolor="r",linewidth=2,align="left")
# # plt.hist(n,color="g",edgecolor="r",linewidth=2,align="right")
# plt.show()







# #HISTTYPE - To change the type of the histogram graph

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# # plt.hist(n,color="g",edgecolor="r",linewidth=2,histtype="step")
# # plt.hist(n,color="g",edgecolor="r",linewidth=2,histtype="stepfilled")
# # plt.hist(n,color="g",edgecolor="r",linewidth=2,histtype="bar")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,histtype="barstacked")
# plt.show()







# #ORIENTATION PARAMETER - To change the orientation of the histogram graph:(vertical , horizontal)

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
#                #to draw horizontal graph
# # plt.hist(n,color="g",edgecolor="r",linewidth=2,orientation="horizontal")
#               #to draw vertical graph
# # plt.hist(n,color="g",edgecolor="r",linewidth=2,orientation="vertical")          #by default
#              #to draw both in a one graph
# plt.hist(n,color="g",edgecolor="r",linewidth=2,orientation="horizontal")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,orientation="vertical")
# plt.show()







# #TO ADJUST WIDTH OF BINS OR BARS     parameter (rwidth)

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,rwidth=0.8)
# plt.show()








# #LOG PARAMETER - To make y - axis or frequency in terms of log

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,log=True)
# plt.show()








# #TO ADD LABEL TO THE GRAPH (label parameter)

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,label="Python")
# plt.legend()
# plt.show()







# #DRAW LINE BETWEEN THE GRAPH TO INDENTIFY THE USEFUL DATA (axvline method)

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,label="Anuj")
# plt.axvline(40,color="black",label="USEFULL DATA",linewidth=2)
# plt.legend()
# plt.show()








#TO ADD GRID TO THE GRAPH

# plt.xlabel("numbers")
# plt.ylabel("numbers2")
# plt.title("HISTOGRAM")
# plt.hist(n,color="g",edgecolor="r",linewidth=2,label="Anuj")
# plt.grid()
# plt.legend()
# plt.show()


