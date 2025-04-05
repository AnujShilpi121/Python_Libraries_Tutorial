import pandas as pd
import os

#  ACCESING LIST DATA IN PANDAS SERIES DATASTRUCTURE

l = [1,4,5,3,6]

# var1 = pd.Series(l)
# var2= pd.Series(l,index=['a','s','d','f','g'])
# var3= pd.Series(l,index=['a','s','d','f','g'],dtype="float")
# var4= pd.Series(l,index=['a','s','d','f','g'],dtype="float",name="Anuj")
#
# print(var1)
# print(var2)
# print(type(var1))
# print(var1[2])
# print(var2['d'])
# print(var3.dtype)
# print(var4)



#  ACCESING DATA FROM ANOTHER DIRECTORY IN PANDAS SERIES DATA STRUCTURE

# var2 = r"C:\Users\dell\Desktop\testing"
# d = os.chdir(var2)
# l = os.listdir(d)
# var3 = pd.Series(l)
# print(var3)



#ACCESING DICTIONARY DATA IN PANDAS SERIES DATA STRUCTURE

# dic = {"name":['python','C++','C','java'],"position":[1,2,3,5,4],"rank":[1,4,3,2]}
# p = pd.Series(dic)
# print(p)

# a  = pd.Series(121)
# b = pd.Series(121,index=[1,2,3,4,5,6])
# print(a)
# print(b)


# s1 = pd.Series(121,index=[1,2,3,4,5,6,7,8])
# s2 = pd.Series(121,index=[1,2,3,4])
# print(s1+s2)








