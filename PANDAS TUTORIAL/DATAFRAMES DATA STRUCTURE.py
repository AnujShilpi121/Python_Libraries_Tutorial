import pandas as pd
# a= pd.DataFrame()
# print(a)


#  ACCESING LIST DATA IN PANDAS DATAFRAME DATASTRUCTURE

# l= [1,2,3,4,5]
# var = pd.DataFrame(l)
# var = pd.DataFrame(l,columns=["A"])
# print(var)
# var = pd.DataFrame(l,columns=["D"])
# print(var)
# print(type(var))



#  ACCESING DICTIONARY DATA IN PANDAS DATAFRAME DATASTRUCTURE

# dic = {"a":[1,2,3,4,5,6],"b":[9,7,8,5,4,6],1:[2,8,6,4,5,6]} # length of all array or all coulumns must be same
# var1 = pd.DataFrame(dic)
# var2 = pd.DataFrame(dic,columns=["a",1])
# var3 = pd.DataFrame(dic,columns=["a",1],index=["a","b","c","d","e","f"])
# var4 = pd.DataFrame(dic,columns=["a",1],index=["a","b","c","d","e","f"],dtype="float")


# print(var1)
# print(var2)
# print(var3)
# print(var4)
# print(var1["a"][3])



#ACCESING THE LIST OF LIST IN DATAFRAME DATASTRUCTURE

# l = [[1,2,3,5,4],[6,8,9,7,1],[11,22,33,44,55],[78,74,54,65,99]]
# a = pd.DataFrame(l)
# print(a)


#CREATING DATAFRAME USING SERIES DATA STRUCTURE OR SERIES FUNCTION

# sr = {"a":pd.Series([1,2,3,4,5]),"b":pd.Series([44,22,33,44,55])}
# pd =  pd.DataFrame(sr)
# print(pd)




#ARITHMETICS OPERATORS IN PYTHON PANDAS

# a = pd.DataFrame({"A":[1,5,6,4,7],"B":[2,5,8,9,5]})
# print(a)
# a["C"] = a["A"] + a["B"]
# a["D"] = a["A"] - a["B"]
# a["E"] = a["A"] * a["B"]
# a["F"] = a["A"] / a["B"]
# print(a)





#CHECKING CONDITIONS IN DATAFRAME
# a = pd.DataFrame({"A":[1,5,6,4,7],"B":[2,5,8,9,5]})
# a["C"] = a["A"]<=2
# a["D"] = a["A"]>=2
# print(a)





#DELETE AND INSERT FUNCTIONS IN DATAFRAME

# a = pd.DataFrame({"A": [1, 5, 6, 4, 7], "B": [2, 5, 8, 9, 5]})

# b = a.insert(1,"C",a["A"])     #insert method returns None
# print(a)
        #or
# a.insert(1,"C",a["A"])
# print(a)

# a.insert(1,"Cat",a["A"][:2])
# print(a)

# c = a.insert(1,"D",{"S":[11,22,33,44,55]})
# d = a.insert(1,"E",[11,22,33,44,55])
# x = [1,2,3,6,5]
# z = {"S":[1,1,1,1,1]}
# e = a.insert(1,"F",x)
# f = a.insert(1,"S",z["S"])
# print(a)



#COPYING SPECIFIED DATA OF ANOTHER COLUMN

a = pd.DataFrame({"A": [1, 5, 6, 4, 7], "B": [2, 5, 8, 9, 5]})
# a["C"] = a["A"][:3]
# print(a)

# b = a.copy()
# print(b)



#DELETING DATA FROM DATAFRAME

# a = pd.DataFrame({"A": [1, 5, 6, 4, 7], "B": [2, 5, 8, 9, 5],"C":[11,22,33,44,55]})

# d = a.pop("B")

# del a["A"]
# print(d)
# print(a)


















