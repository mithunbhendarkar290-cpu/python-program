# program 1
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Array:",arr)

#program 2
import numpy as np
print("Zeros:\n",np.zeros((2,2)))
print("Ones:\n",np.ones((3,3)))
print("Full:\n",np.full((2,2),7))
print("Random:\n",np.random.rand(2,2))

#program 3
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Element:",arr[1][2])
print("Slice:\n",arr[0:2, 1:3])
new_arr = arr.reshape(1, 9)
print("Resphaped:",new_arr)

#program 4
import numpy as np
a= np.array([1, 2, 3])
b= np.array([4, 5, 6])
print("Addition:",a + b)
print("Multiplication:",a * b)
print("Mean:",np.mean(a))
print("Sum:",np.sum(b))
      
    
      