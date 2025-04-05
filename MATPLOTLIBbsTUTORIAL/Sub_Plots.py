import matplotlib.pyplot as plt

#BASIC SYNTAX
           #linear plot
x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]
plt.subplot(2,2,1)           #plt.subplot(nrows,ncols,index)
plt.plot(x,y,color="b")


           #dot pie plot
plt.subplot(2,2,2)
plt.pie([1],colors="r")

           #pie plot
plt.subplot(2,2,3)
plt.pie([10,20,30,40])


           #bar plot
x1 = [1,2,3,4]
y1 = [10,20,30,40]
plt.subplot(2,2,4)
plt.bar(x1,y1)


plt.show()