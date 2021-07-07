
def divisiblenum(array, n):
	remainder = 0
	for i in range (0, n):
		remainder = ( remainder + array[i]) % 5
	return (remainder == 0)


array = [4,51, 90,23,42];
n = 5
if (divisiblenum(array, n)):
	print("Yes")
else:
	print("No")