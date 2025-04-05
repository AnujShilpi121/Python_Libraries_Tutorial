
import pandas as pd
# a = {"A": [1, 5, 6, 4, 7], "B": [2, 5, 8, 9, 5],"C":[11,22,33,44,55]}

# d= pd.DataFrame(a)

# # #CONVERTING INTO CSV FILE
# d.to_csv("Test_new.csv")

# # #REMOVING INDEX FROM CSV FILE
# d.to_csv("Test_new1.csv",index=False)

# # #CHANGING THE NAME OF THE COLUMNS OF CSV FILE
# d.to_csv("Test_new2.csv",columns=["A","B"])    #to print specific columns

# d.to_csv("Test_new2.csv",header=["1a","2c","3c"])








#READING CSV FILES

import pandas as pd
# csv_1 = pd.read_csv ("D:\\PANDAS TUTORIAL\\Test_new2.csv")
# print(csv_1)
# csv_2 = pd.read_csv ("D:\\sample.csv")
# print(csv_2)
# csv_3 = pd.read_csv ("D:\\sample.csv",nrows=2)
# csv_3 = pd.read_csv ("D:\\sample.csv",usecols=[1,3])
# print(csv_3)
# csv_4 = pd.read_csv ("D:\\sample.csv",skiprows=[4,5])
# print(csv_4)
# csv_5 = pd.read_csv ("D:\\sample.csv",index_col=[2])
# print(csv_5)
# csv_6 = pd.read_csv ("D:\\sample.csv",header=4)
# print(csv_6)
# csv_7 = pd.read_csv ("D:\\sample.csv")
# print(csv_7)
# csv_8 = pd.read_csv ("D:\\sample.csv",names=["col1","col2"])
# print(csv_8)
# csv_8 = pd.read_csv ("D:\\sample.csv",names=["col1","col2","col3","col4","col5"])
# print(csv_8)

# csv_9 = pd.read_csv ("D:\\sample.csv",header=None)
# print(csv_9)

# csv_10 = pd.read_csv ("D:\\sample.csv",header=None,prefix="col")
# print(csv_10)
# csv_11 = pd.read_csv ("D:\\sample.csv",dtype={"Salary":"float"})
# print(csv_11)





#METHODS AND ATTRIBUTES OF PANDAS CSV FILES
csv_7 = pd.read_csv ("D:\\sample.csv")
# print(csv_7)

# print(csv_7.index)                     #returns range of indexing

# print(csv_7.columns)

# print(csv_7.describe())               #Returns description of each column as (mean,count,......)

# print(csv_7.head())                  #Returns top 5 index data or top 5 rows
# print(csv_7.head(7))

# print(csv_7[:8:2])                   #Slicing

# print(csv_7.index.array)             #Returns array of indexes

# print(csv_7.to_numpy())              #Returns 2-dimentional array of data
      #or
# import numpy as np
# print(np.array(csv_7))

# print(csv_7.sort_index(axis=0,ascending=False))          #Returns data in decending order

                          #Accessing and changing data of a particular location

# csv_7["Name"][0] = "python"                #To change the data of a particular location
# print(csv_7)
        #or
# csv_7.loc[0,"Name"] = "python"
# print(csv_7)

# print(csv_7.loc[0,"Name"])

# print(csv_7.loc[[1,6],["Name","Dept"]])
# print(csv_7.loc[:,["Name","Dept"]])
# print(csv_7.loc[1:3,:])
# print(csv_7.loc[:,["Name","Dept"]])
# print(csv_7.loc[:,["Name","Dept"]])
# csv_7.iloc[1,3] = "python"
# print(csv_7.iloc[:,:])                #in iloc both arg should be index as row index,col index
# print(csv_7)

                              #Droping data from dataset
# a=csv_7.drop(1,axis=0)
# print(a)
# print(csv_7.drop("Name",axis=1))
# print(csv_7)






#HANDLING MISSING DATA USING DROPNA AND FILLNA FUNCTION

# csv_7 = pd.read_csv("D:\\sample.csv")
# print(csv_7)
# a = csv_7.dropna()
# a=csv_7.dropna(axis=0)
# a=csv_7.dropna(axis=1)
# a=csv_7.dropna(how="any")
# a=csv_7.dropna(how="all")
# a=csv_7.dropna(subset=["Salary"])
# csv_7.dropna(inplace=True)
# print(csv_7)
# a=csv_7.dropna(thresh=2)
# print(a)

# a = csv_7.fillna("python")
# a = csv_7.fillna({"Company":"222222","Dept":"Anuj"})
# a = csv_7.fillna(method='ffill')
# a = csv_7.fillna(method='ffill',axis=0)
# a = csv_7.fillna(method='ffill',axis=1)
          #or
# a = csv_7.ffill()


# a = csv_7.fillna(method='bfill')
# a = csv_7.fillna(method='bfill',axis=0)
# a = csv_7.fillna(method='bfill',axis=1)

# a = csv_7.fillna("anuj",limit=2)                  #Fill limited NaN values as given
# a = csv_7.fillna("anuj",limit=2,axis=0)
# a = csv_7.fillna("anuj",limit=2,axis=1)
# print(a)

# csv_7.fillna(12,inplace=True)              #fill NaN values witth the given value
# print(csv_7)






#REPLACE AND INTERPOLATE FUNCTION
                    #METHOD REPLACE
# csv_7 = pd.read_csv("D:\\sample.csv")
# print(csv_7)

# var=csv_7.replace(454445,111111111)
# var=csv_7.replace(["gfdgdf","gfdfgf","nbm","ghh"],"Anuj")            #Replacing multiple values
# var=csv_7.replace("[a-zA-Z]","Anuj",regex=True)
# var=csv_7.replace({"Company":"[a-zA-Z]"},55555555,regex=True)                #Replacing specific columns data
# print(var)

# var = csv_7.replace( 56,method="ffill")
# var = csv_7.replace( 56,method="ffill",limit=2)
# print(var)

# var = csv_7.replace( 56,method="bfill")
# var = csv_7.replace( 44,method="bfill",limit=2)
# print(var)

# csv_7.replace( 56,method="ffill",inplace=True)               #use inplace keyword when you do not want to make copy of the dataset
# print(csv_7)


                       #METHOD INTERPOLATE   ----   Fill only integer NaN values
# csv_7 = pd.read_csv("D:\\sample.csv")
# print(csv_7)
# print(csv_7.interpolate())
# print(csv_7.interpolate(method="linear"))
# print(csv_7.interpolate(method="linear",axis=0))
# print(csv_7.interpolate(method="linear",axis=1))             #Fill when all colums having integer values
# print(csv_7.interpolate(limit=2))
# print(csv_7.interpolate(limit_direction="forward",limit=2))
# print(csv_7.interpolate(limit_direction="backward",limit=2))
# print(csv_7.interpolate(limit_direction="both",limit=2))
# print(csv_7.interpolate(limit_area="inside"))
# print(csv_7.interpolate(limit_area="outside"))

# csv_7.interpolate(limit_area="outside",inplace=True)                #when do not want to make the copy of the dataset
# print(csv_7)








                      #MERGING  DATAFRAMES    ----   Merge two dataframe only when both dataframe having same or common column

# var1 = pd.DataFrame({"A":pd.Series([1,2,3,4]),"B":pd.Series([11,21,33,44])})
# var2 = pd.DataFrame({"A":pd.Series([1,2,3,4]),"C":pd.Series([21,22,23,24])})
# print(pd.merge(var1,var2))
        #or
# print(pd.merge(var1,var2,on="A"))


          #When common column having different element then it will merge only those rows of common column which have same element
# var1 = pd.DataFrame({"A":pd.Series([1,2,3,4]),"B":pd.Series([11,21,33,44])})
# var2 = pd.DataFrame({"A":pd.Series([14444,2,3333,4]),"C":pd.Series([21,22,23,24])})
# print(pd.merge(var1,var2))
# print(pd.merge(var1,var2,how="inner"))
# print(pd.merge(var1,var2,how="outer"))
# print(pd.merge(var1,var2,how="left"))
# print(pd.merge(var1,var2,how="right"))
# print(pd.merge(var1,var2,how="right",indicator=True))             #To check which data is  merged


         #To merge when both dataframes having same column name
# var1 = pd.DataFrame({"A":pd.Series([1,2,3,4]),"B":pd.Series([11,21,33,44])})
# var2 = pd.DataFrame({"A":pd.Series([14444,2,3333,4]),"B":pd.Series([21,22,23,24])})
# print(pd.merge(var1,var2,on="A"))
# print(pd.merge(var1,var2,left_index=True,right_index=True))
# print(pd.merge(var1,var2,left_index=True,right_index=True,suffixes=("name","python")))         #To change the column name






                    #CONCATING TWO DATAFRAMES   ----    concatenate the two dataframes and series as well

      #SERIES
# s1 = pd.Series([1,2,3,4])
# s2 = pd.Series([11,22,33,44,55])
# print(pd.concat([s1,s2]))

    #DATAFRAME
# d1 = pd.DataFrame({"A":pd.Series([1,2,3,4]),"B":pd.Series([11,21,33,44])})
# d2 = pd.DataFrame({"A":pd.Series([2,3333,4]),"B":pd.Series([21,22])})
# print(pd.concat([d1,d2]))
# print(pd.concat([d1,d2],axis=0))
# print(pd.concat([d1,d2],axis=1))
# print(pd.concat([d1,d2],axis=1,join="inner"))
# print(pd.concat([d1,d2],axis=1,join="outer"))
# print(pd.concat([d1,d2],keys=["d1","d2"],axis=1))             #To give name of both dataframe







                #METHOD GROUPBY  ----    Used for making group of similar element on the basis of column
# var = pd.DataFrame({"Name":["a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d"],
#                     "sub1":[25,25,33,66,88,55,99,66,33,22,44,77,55,22,55,12],
#                     "sub2":[21,22,13,66,81,55,99,12,33,22,44,77,55,92,65,12]}
#                    )
# var1 = var.groupby("Name")
# for x,y in var1:
#     print(x)
#     print(y)
#     print("\n")

                 #To get specific group
# print(var1.get_group("a"))
# print(var1.get_group("b"))
# print(var1.get_group("c"))
# print(var1.get_group("d"))

                #Some methods of group
# print(var1.max())
# print(var1.min())
# print(var1.mean())


              #To make list of group
# print(list(var1))







                         #JOINING TWO DATAFRAMES

# d1 = pd.DataFrame({"A":pd.Series([1,2,3,4]),"B":pd.Series([11,21,33,44])})
# d2 = pd.DataFrame({"C":pd.Series([2,3333,4]),"D":pd.Series([21,22])})
# print(d1.join(d2))

# d1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,21,33,44]},index=["a","b","c","d"])
# d2 = pd.DataFrame({"C":[2,3333],"D":[21,22]},index=["a","b"])
# print(d1.join(d2))
# print(d1.join(d2,how="left"))
# print(d1.join(d2,how="right"))
# print(d1.join(d2,how="inner"))
# print(d1.join(d2,how="outer"))

                          #If column having same names
# d1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,21,33,44]},index=["a","b","c","d"])
# d2 = pd.DataFrame({"C":[2,3333],"B":[21,22]},index=["a","b"])
# print(d1.join(d2,lsuffix="_12"))
# print(d1.join(d2,rsuffix="_12"))
# print(d1.join(d2,rsuffix="_12",lsuffix="_121"))








                         #APPENDING TWO DATAFRAMES    ----   Append the values of two column having same name in one column
# d1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,21,33,44]})
# d2 = pd.DataFrame({"C":[2,3333],"B":[21,22]})
# print(d1.append(d2))
# print(d1.append(d2,ignore_index=True))







                  #METHOD MELT  AND PIVOT  ----   USED FOR RESHAPE
      #MELT()
# d1 = pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[11,21,33,44,55,88],"maths":[89,89,78,77,55,66]})
# print(d1)
# print(pd.melt(d1))
# print(pd.melt(d1,id_vars="days"))
# print(pd.melt(d1,id_vars="days",var_name="pyhton"))
# print(pd.melt(d1,id_vars="days",var_name="pyhton",value_name="anuj"))
# print(pd.melt(d1,id_vars="days",var_name="pyhton",value_name="anuj",value_vars="eng"))

      #PIVOT()
# d1 = pd.DataFrame({"days":[1,2,3,4,5,6],"st_name":["a","b","c","d","a","b"],"eng":[11,21,33,44,55,88],"maths":[89,89,78,77,55,66]})
# print(d1)
# print(pd.pivot(d1,index="days",columns="st_name"))              #must required index,columns
# print(pd.pivot(d1,index="days",columns="st_name",values="eng"))

      #PIVOT_TABLE()
# print(pd.pivot_table(d1,index="days",columns="st_name"))
# print(pd.pivot_table(d1,index="days",columns="st_name",aggfunc="mean"))
# print(pd.pivot_table(d1,index="days",columns="st_name",aggfunc="sum"))
# print(pd.pivot_table(d1,index="days",columns="st_name",aggfunc="count"))
# print(pd.pivot_table(d1,index="days",columns="st_name",aggfunc="min"))
# print(pd.pivot_table(d1,index="days",columns="st_name",aggfunc="max"))
# print(pd.pivot_table(d1,index="days",columns="st_name",aggfunc="max",margins=True))


                      # READING JSON DATA

# import pandas as pd
# a = pd.read_json("D:\\data.js")
# print(a)
# print(type(a))
# b = pd.DataFrame(a)
# print(type(b))
# print(b)


# CONVERTING JSON DATA TO DATAFRAME
# data = {
#     "A":{
#         "a":60,
#         "b":50
#      },
#     "B":{
#         "c":45,
#         "d":89
#         }
#     }
# print(type(data))
# c = pd.DataFrame(data)
# print(c)






