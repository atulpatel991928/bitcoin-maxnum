import numpy as np

def maxnum(array,n):
    max=0
    for i in range(0, len(array)):
        if (array[i] > max):
            max = array[i]  #updates max here
    return max

atul= [1,15,25,45,42,21,17,12,11]
nitesh= [3, 5, 8, 7, 9, 19, 10]
print(maxnum(atul, len(atul)))
print(maxnum(nitesh, len(nitesh)))

print(atul)
print(nitesh)








