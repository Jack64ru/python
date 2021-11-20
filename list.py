c = [1, 2, 3, 31]
k = [4, 5, 6, 11]
n = []
for i in c:
    if i % 2 != 0:
        n.append(i)
for j in k:
    if j % 2 == 0:
        n.append(j)
n.sort()
print(n)