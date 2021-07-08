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