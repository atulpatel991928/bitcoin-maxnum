import numpy
print (numpy.__version__)

list1 =[1,2,3,4,5]
key = 4
num = len(list1)

def linear_search(list1, num, key):
    for i in range(0, num):
        if (list1[i] == key):
            return i
    return -1

res=linear_search(list1,num,key)


if(res==-1):
    print("Element not found:",)
else:
    print("Element found in index:", res)
