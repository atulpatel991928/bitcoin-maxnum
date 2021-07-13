l = []
l.append(5)
l.append(2)
l.append(6)
l.pop()
l.pop()
l.append(132)
l.append(4)
l.append(-5)
print(l)

last=l.pop()
l.sort(reverse=True)
print("sorted list:", l)
print(last)





















