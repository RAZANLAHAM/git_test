import numpy as np
import matplotlib.pyplot as plt
# Q1 :
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("the original matrix :")
print(matrix)
print('#' * 50)
transpose = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
])
# transpose is found by interchange rows into columns and opposit of this:T
# nested loop method
for i in range(len(matrix)):  # length of rows 0 to 2
    for j in range(len(matrix[0])):  # represented the columns 0 to 2
        transpose[j][i] = matrix[i][j]
print(transpose)
print('#' * 50)
# by using transpose fun :
print("2nd method of transpose :")
print(np.transpose(matrix))
# the determinant of a matrix :
print('#' * 50)
det = np.linalg.det(matrix)
print("the det is :")
print(int(det))
print('#' * 50)
# the inverse :
if det != 0:
    print("it has an inverse")
    inverse = np.linalg.inv(matrix)
else:
    print("the matrix does not have an inverse")

# Q2 :
print('#' * 50)
print("Q2")
X = ("Category A", "Category B", "Category C", "Category D")
Y =(10, 25, 15, 30)
plt.title("Bar Chart Example")
fig = plt.bar(X,Y)
plt.xlabel("category")
plt.ylabel("values")
plt.show()
X = (1, 2, 3, 4, 5)
Y = (5, 7, 4, 2, 8)
plt.title("Scatter Plot Example")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
fig = plt.scatter(X,Y)
plt.show()
# Q3:
count = 0
num = np.array[011000]
for i in range(len(num)):
    if num[i] == 0:
        count +=1

print("num of 0 =")
print(count)





