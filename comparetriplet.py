from functools import reduce
from numpy import *
a = list(map(int, input('triplet a').rstrip().split()))

b = list(map(int, input('triplet b').rstrip().split()))

c =[]
d =[]
x=1
for i in  range(3):

    if a[i]>b[i]:
        c.append(x)
    elif a[i]==b[i]:
        a.append(0)
        b.append(0)
    else :
        d.append(x)
if c==[]:
    c.append(0)
if d==[]:
    d.append(0)

result = [reduce(lambda x, y: x + y, c) , reduce(lambda t, y: t + y, d)]

print(result)