import numpy as np

              # 1 dimentional array
'''
# arr = np.array([1,2,3,4])
arr = np.array([1,2,3,4],np.int8)   #size of integer value defined as int8 , int 32 .......
print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.size)
'''



              # 2 dimentional array

# arr = np.array([[1,2,3,4]])
# arr = np.array([[1,2,3,4]],np.int8)
# arr = np.array([[1,2,3,4],[4,5,6,5],[4,8,9,6]])
# print(arr)
# print(arr.shape)
# print(arr.dtype)
# print(arr.size)







          #TAKING INPUT IN AN ARRAY
   # 1-dimentional array
# arr = np.empty((5),dtype=int)
# for i in range(5):
#     element = int(input())
#     arr[i] = element
# print(arr)

     # 2-dimentional array
# arr1 = np.empty((5,3),dtype=int)
# for i in range(5):
#     for j in range(3):
#         element = int(input())
#         arr1[i][j] = element
# print(arr1)






                        # JOINING NUMPY ARRAYS USING (concatenate(),stack())
               # 1-dimentional array
     #concatenate()

# arr = np.array([1,2,3,4,5,6])
# arr1 = np.array([1,2,3,4,5,6])
# print(np.concatenate((arr,arr1)))
# print(np.concatenate((arr,arr1),axis=0))


     #stack() -- return two dimentional array only

# arr = np.array([1,2,3,4,5,6])
# arr1 = np.array([1,2,3,4,5,6])
# print(np.stack((arr,arr1)))
# print(np.stack((arr,arr1),axis=0))
# print(np.stack((arr,arr1),axis=1))


               # 2-dimentional array
# concatenate()

# arr = np.array([[1,2,3],[4,5,6]])
# arr1 = np.array([[1,2,3],[4,5,6]])
# print(np.concatenate((arr,arr1)))
# print(np.concatenate((arr,arr1),axis=0))
# print(np.concatenate((arr,arr1),axis=1))


# stack()

# arr = np.array([[1,2,3],[4,5,6]])
# arr1 = np.array([[2,2,3],[4,5,6]])
# print(np.stack((arr,arr1)))

# print(np.hstack((arr,arr1)))           #rows
# print(np.vstack((arr,arr1)))          #columns
# print(np.dstack((arr,arr1)))          #height

# print(np.stack((arr,arr1),axis=0))
# print(np.stack((arr,arr1),axis=1))





                 #method array_split()         # returns a list containing splitted arrays
      # 1-dimentional array
# arr = np.array([1,2,3,4,5,6])
# ar = np.split(arr,3)
# print(ar[0])

     # 2-dimentional array
# arr = np.array([[1,2,3,1],[3,4,1,3],[1,5,6,4]])
# ar = np.split(arr,3)
# ar = np.split(arr,3,axis=0)
# ar = np.split(arr,4,axis=1)
# print(ar)
# print(ar[1])






                # method copy() and view()
     #copy()
# arr = np.array([1,2,3,4,56,6])
# co = arr.copy()
# print('arr :',arr)
# print('co :',co)
#
# arr[1] = 22222
# print('arr :',arr)
# print('co :',co)

     #view()           --       if we change the original data the view data also changes
# arr = np.array([1,2,3,4,56,6])
# vi = arr.view()
# print('arr :',arr)
# print('co :',vi)
#
# arr[1] = 22222
# print('arr :',arr)
# print('co :',vi)






                    #method insert() ,append() and delete()

             # method insert()    -   can't insert float values

     # 1-dimentional
# arr = np.array([1,2,3,4,5,6])
# print(arr)

# ar = np.insert(arr,2,77)
# print(ar)

# ar1 = np.insert(arr,(2,3),77)
# print(ar1)

# ar2 = np.insert(arr,(2,3),77.5)           # insert only integer part of float value
# print(ar2)

       # 2-dimentional
# arr = np.array([[1,2],[3,4],[5,6]])
# print(arr)

# ar = np.insert(arr,2,77)
# print(ar)

# ar1 = np.insert(arr,(2,3),77)             # inserting value at multiple indexes
# print(ar1)
#
# ar2 = np.insert(arr,(2,3),77.5)           # insert only integer part of float value
# print(ar2)

# ar1 = np.insert(arr,0,77,axis=0)
# print(ar1)

# ar11 = np.insert(arr,(0,1),77,axis=0)             # inserting value at multiple indexes
# print(ar11)

# ar2 = np.insert(arr,(0,1),77.5,axis=1)           # insert only integer part of float value
# print(ar2)



                     # method append()  - can append  interger as well as float values   at the last+1 index
     # 1-dimentional
# arr = np.array([1,2,3,4,5,6])
# print(arr)

# ar = np.append(arr,77.88)
# print(ar)

       # 2-dimentional
# arr = np.array([[1,2],[3,4],[5,6]])
# print(arr)

# ar1 = np.append(arr,(88,77))
# print(ar1)
#
# ar2 = np.append(arr,[[88,77]],axis=0)
# print(ar2)


                       # method - delete()
     # 1-dimentional
# arr = np.array([1,2,3,4,5,6])
# print(arr)
#
# ar = np.delete(arr,2)
# print(ar)

       # 2-dimentional
# arr = np.array([[1,2],[3,4],[5,6]])
# print(arr)
#
# ar1 = np.delete(arr,(1),axis=0)
# print(ar1,'\n')
# 
# ar2 = np.delete(arr,(1),axis=1)
# print(ar2)



                    # method zeros()

# zeros = np.zeros((2,8))       # 2 dimentional
# zeros = np.zeros([2,8])       # 2 dimentional
# zeros = np.zeros(5)           # 1 dimentional
# print(zeros)
# print(zeros.shape)
# print(zeros.dtype)
# print(zeros.size)




       #method arange() - (full form = arrayrange)   return an array containing elements of given range
# arr = np.arange(15)         # end index
# arr = np.arange(5,15)       #intial and end index

# arr = np.arange(5,15,5)    # intial , end, steps
# print(arr)





            #method linspace()  - (fullform = linearspace)
# lspace = np.linspace(1,5,12)       #intial num , final num , how many numbers you want to print
# print(lspace)





            #method empty() - return an empty array with garbage elements  of given size
      # 1 - dimentional
# em = np.empty([5,8])           # row , column
# em = np.empty((5,8))           # row , column
# em[1,1]  = 454
# print(em)

     # 2 - dimentional
# em = np.empty(5)
# print(em)




           #method empty_like() - return an empty array like given parameter
# lspace = np.linspace(1,5,12)
# emp_like = np.empty_like(lspace)
# print(emp_like)

# emp_like[1]  = 454
# print(emp_like)






               #method identity()  - return an identity array or an identity matrix
# iden = np.identity(5)
# print(iden)
# print(iden.shape)





            #method reshape()   -  return an reshaped array (can convert 1 dimentional into 2 dimentional and vice versa)
# arr = np.arange(15)
# print(arr)
# arr1 = arr.reshape(3,5)         #size should be same same
# print(arr1)






            #method ravel()  -  convert 2 dimentional array into 1 dimentional array
# arr = np.array([[1,2,3,4],[5,6,7,9],[11,22,33,44],[55,88,99,77]])
# print(arr)
# print(arr.shape)
# arr = arr.ravel()
# print(arr)
# print(arr.shape)






            #method reshape()  -  reshape the array (1 and 2 dimentional both)
     # 1 dimentional
# arr = np.array([1,2,3,4,5,6,7,8])
# r = arr.reshape(2,4)
# print(r)

    # 2 dimentional
# arr = np.array([[1,2,3,4],[5,6,7,8],[11,22,33,44]])
# r = arr.reshape(12)
# r = arr.reshape(6,2)
# r = arr.reshape(1,12)
# r = arr.reshape(12,1)
# print(r)





                #method sqrt()   -  return an array containing square rooted elements
#      # 1 - dimentional
# arr1 = np.array([1,2,3,4,5,6])
# sq_root1 = np.sqrt(arr1)
# print(sq_root1)
#
#    # 2 - dimentional
# arr2 = np.array([[1,2,3],[4,4,4],[9,9,9]])
# sq_root2 = np.sqrt(arr2)
# print(sq_root2)





             #method sum()  -  return total sum of elements of an array
#      # 1 - dimentional
# arr1 = np.array([1,2,3,4,5,6])
# print(arr1.sum())
#
#      # 2 - dimentional
# arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2.sum())                # return total sum of elements of an array
# print(arr2.sum(axis=1))          # return an array containing sum of axis 1 elements
# print(arr2.sum(axis=0))          # return an array containing sum of axis 0 elements







               #method where()  -  return an index of element if available in the array (used to find the elemnt in the array)
       # 1 - dimentional
# arr = np.array([1,23,4,5,6,85,8])
# print(np.where(arr>5))                   #return an array
# print(np.argwhere(arr>5))                #return ndarray

    # 2 - dimentional
# arr = np.array([[1,23,4],[1,2,3],[5,8,9]])
# print(np.where(arr>5))                     #return array of row index and array of column index
# print(np.argwhere(arr>5))                  #return ndarray





                 #method count_nonzero()  -  return count of non zero elements of an array
       # 1 - dimentional
# arr1 = np.array([1,23,4,5,6,85,8,0,0])
# print(np.count_nonzero(arr1))
# print(np.nonzero(arr1))

     # 2 - dimentional
# arr2 = np.array([[1,23,0],[1,2,3],[5,8,9]])
# print(np.count_nonzero(arr2))
# print(np.nonzero(arr2))






                   #method - tolist()   -   convert array into list
       # 1 - dimentional
# arr1 = np.array([1,23,4,5,6,85,8,0,0])
# print(arr1.tolist())

     # 2 - dimentional
# arr2 = np.array([[1,23,0],[1,2,3],[5,8,9]])
# print(arr2.tolist())





            #axis parameter
# lis = [[1,2,3,4],[5,6,9,8],[1,1,1,1]]
# arr = np.array(lis)
# print(arr)

# s = arr.sum(axis=0)
# print(s)
#
# s = arr.sum(axis=1)
# print(s)






             #some other attributes
'''
arr = np.array([[1,2,3,4],[5,6,9,8],[1,1,1,1]])
arr1 = np.array([1,2,3,4,5,6,7])
print(arr,"\n")

# print(arr.T)         #Transpose the array or matrix

# arr_flat = arr.flat      #Flatten the array or matrix (it is an iter object)
# for item in arr_flat:
#     print(item)


# print(arr.ndim)           #returns number of dimention of an array
# print(arr1.ndim)
#
# print(arr.size)           #returns size of the array (no of element)
#
# print(arr.dtype)           #return datatype of the elements of the array
#
# print(arr.shape)           #returns shape of the array (num. of rows and columns)
#
# print(arr.nbytes)          #return number of bytes consumed by an array

print(arr.itemsize)        #return size of element of an array  in byte

print(arr.size)            #return size of array in bytes
'''




              #SOME OTHER FUNCTIONS OR METHODS
      # 1 - dimentional
# one = np.array([5,55,8,9,6,7,33])
# print(one.argmax())             #returns index of largest element

# print(one.argmin())             #returns index of smallest element

# print(one.argsort())            #returns list of indexes in sorting order
# print(one.argsort(axis=0))

# print(one.max())              #return largest element of an array
# print(one.min())              #return smallest element of an array
# print(np.sort(one))           #return sorted array

     # 2 - dimentional
# two = np.array([[1,2,3],[5,1,2],[88,6,9]])
# print(two.argmax())                 #return an index of largest element
# print(two.argmax(axis=0))           #return an array containing indexes of largest element of an array of axis 0
# print(two.argmax(axis=1))           #return an array containing indexes of largest element of an array of axis 1

# print(two.argmin())                 #return an index of smallest element
# print(two.argmin(axis=0))           #return an array containing indexes of smallest element of an array of axis 0
# print(two.argmin(axis=1))           #return an array containing indexes of smallest element of an array of axis 1

# print(two.argsort())                #by default axis = 1
# print(two.argsort(axis=0))          #return an array containing sorted indexes of an array of axis 0
# print(two.argsort(axis=1))          #return an array containing sorted indexes of an array of axis 1

# print(two.max())                    #return max element of an array
# print(two.max(axis=0))              #return an array containing largest element of axis 0
# print(two.max(axis=1))              #return an array containing largest element of axis 1
#
# print(two.min())                    #return min element of an array
# print(two.min(axis=0))              #return an array containing smallest element of axis 0
# print(two.min(axis=1))              #return an array containing smallest element of axis 1

# print(np.sort(two))                  #return sorted array containing sorted elements
# print(np.sort(two,axis=0))           #return sorted array containing sorted elements of axis 0
# print(np.sort(two,axis=1))           #return sorted array containing sorted elements of axis 1






                #Operations on array
     # 1 dimentional
# arr1 = np.array([1,2,3,3,2,2,5])
# arr2 = np.array([1,2,3,4,5,6,7])
# print(arr1+arr2)
# print(arr1-arr2)
# print(arr1*arr2)
# print(arr1/arr2)
# print(arr1//arr2)

     # 2 dimentional
# arr1 = np.array([[1,2,3],[5,4,1],[8,1,1]])
# arr2 = np.array([[1,2,3],[1,1,1],[2,2,2]])
# print(arr1+arr2)
# print(arr1-arr2)
# print(arr1*arr2)
# print(arr1/arr2)
# print(arr1//arr2)








