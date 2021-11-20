i = int(input('number: '))
k = 0
for p in range(i+1):
    if p % 3 == 0 or p % 5 == 0:
        k += p
    else:
        continue
print(k)
