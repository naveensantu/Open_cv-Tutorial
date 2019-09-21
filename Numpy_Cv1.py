import numpy as np
mylist=["naveen",123,"random123","random_12_#"]
type(mylist)

myarray=np.array(mylist)
type(myarray)

np.arange(0,10,2)
np.zeros(shape=(1,5))
np.ones((1,4))

np.random.seed(101)
arr=np.random.randint(0, 100, 10, dtype='l')
arr
arr2=np.random.randint(0,100,10)
arr2

arr.max()
arr.argmax()
arr.min()
arr.argmin()
arr.shape
arr.reshape((2,5))
mat=np.arange(0,100).reshape(10,10)
mat
row=4
col=6
mat[row,col]
mat[:,3]
mat[:,3].reshape(2,5)
mat[2,:]
mat[4:7,4:10]
newmat=mat.copy()
newmat[0:6,:]=999
newmat
