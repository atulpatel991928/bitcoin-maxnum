
import numpy as np
def minnum(array,n):
    min=1000000
    for i in range(0, len(array)):
        if (array[i] < min):
            min= array[i]
    return min
atul= [14,15,25,45,42,21,17,12,11]
nitesh= [3, 5, 8, 7, 9, 19, 10]
print(minnum(atul, len(atul)))
print(minnum(nitesh, len(nitesh)))

# Program to add two matrices using nested loop

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]


result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)):
# iterate through columns
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]

for r in result:
	print(r)
