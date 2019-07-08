from numpy import *
from functools import reduce

arr = array([
    [11, 0, 4],
    [2, 5, 4],
    [10, 1, -12]
])
a = []
b = []


for i in range(3):
    x = arr[i][2-i]
    a.append(x)

for j in range(3):
    y = arr[j][j]
    b.append(y)

c = reduce(lambda a, b: a + b, b) - reduce(lambda c, d: c + d, a)

print(c)

