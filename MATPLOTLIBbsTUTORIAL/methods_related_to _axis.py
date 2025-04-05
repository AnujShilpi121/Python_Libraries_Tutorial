import matplotlib.pyplot as plt
# x = [1,2,3,4,5,6]
# y = [10,12,3,4,5,6]
# plt.plot(x,y,color="b")
# plt.show()



#REPLACING THE VALUES OF X-AXIS AND Y-AXIS
# x = [1,2,3,4,5,6]
# y = [10,12,3,4,5,6]
# plt.plot(x,y,color="b")
# plt.xticks(x,["python","c++","java","c#","c","javascripts"])
# plt.yticks(y,["a","b","c","d","e","f"])
# plt.show()






#SETTING LIMITS OF X-AXIS AND Y-AXIS
# x = [1,2,3,4,5,6]
# y = [10,12,3,4,5,6]
# plt.plot(x,y,color="b")
# plt.xlim(0,20)
# plt.ylim(0,20)
# plt.show()

                #OR

x = [1,2,3,4,5,6]
y = [10,12,3,4,5,6]
plt.plot(x,y,color="b")
plt.axis((0,20,0,20))
plt.show()


