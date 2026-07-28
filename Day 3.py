import numpy as np
arr1=np.array([80,30,36,45])
print(arr1)
arr2=np.array([[10,30,34], [2,10,30]])
print(arr2)
#Array information
print("shape:",arr2.shape)
print("size:", arr2.size)
print("Dimensions:", arr2.ndim)
print("data types:",arr2.dtype)


#Mathematical operations
import numpy as np
a=np.array([20,30,1])
b=np.array([1,30,50])

print("Multiplication:",a*b)
print("Addition:",a+b)
print("substraction:",a-b)
print("division:",a/b)


#salar opertions
arr = np.array([5, 10, 15])

print(arr + 5)
print(arr * 2)
print(arr / 5)

#practice array calculation
marks=np.array([20,60,40,60,89])
print("marks:",marks)
print("total:",np.sum(marks))
print("seed:",np.mean(marks))
print("highest:",np.max(marks))
print("lowest:",np.min(marks))

#reshape array

arr=np.array([2,6,9,7])
print(arr.reshape(2,2))

#random number
import numpy as np
print(np.random.randint(1,100,1000))