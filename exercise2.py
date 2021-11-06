import math
x1 = float(input('vvedite x1: '))
y1 = float(input('vvedite y1: '))
x2 = float(input('vvedite x2: '))
y2 = float(input('vvedite y2: '))
r = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3)
print(r)