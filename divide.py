def isPossibleToMakeDivisible(arr, n):

	remainder = 0
	for i in range (0, n):
		remainder = (remainder + arr[i]) % 5

	return (remainder == 0)

arr = [40, 50, 90,56,67 ];
n = 3
if (isPossibleToMakeDivisible(arr, n)):
	print("Yes")
else:
	print("No")
