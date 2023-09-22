# numpy : numerical python
import numpy as np
import matplotlib.pyplot as plt

'''
'# The concept :I can write 2D,3D array and show it as an image
print(dir(np))
dir() func :
returns all properties and methods of the specified object, 
without the values.

array = [[1,3,4,9]
    ,[5,0,8,-3]]
   for i in range(len(array)) :# allow us to go through each (row) index in array
    # length of array is 2 which is (0,1) rows
    # we can access each row array [i]
     for j in range(len(i)) : # we can iterate over each index for each item in the row
   print(array[i][j])
   '''

array = np.array(
    [
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],

    ]
)
# The smallest value represents the darkest colour and the largest represents the most light
plt.imshow(array)
plt.show()
# chess board
arr = np.array(
    [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
    ]
)
plt.imshow(arr, cmap='gray')
plt.show()
A = np.array(
    [
        [30,20,30,30],
        [30, 20, 30, 30],
        [30, 20, 30, 30],
        [30, 20, 30, 30],
        [30, 20, 30, 30],
        [30, 20,20,20]

    ]
)
plt.imshow(A, cmap='gray')
plt.show()
# standered for image 0 to 255 number of bits 2 to the power8
