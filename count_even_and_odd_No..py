def evenodd(arr, n):
    evenno = 0
    oddno = 0
    for i in range(n):

        if (arr[i] % 2 == 1):
            oddno += 1
        else:
            evenno += 1

    print("Number of even elements = ",
          evenno)
    print("Number of odd elements = ",
          oddno)

arr = [2, 3, 4, 5, 6,3,56,78,98,76,53]
length = len(arr)
evenodd(arr, length)