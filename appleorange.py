# s, t, a, b, apples m, oranges n
import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    x = []
    y = []
    k = 1

    for i in range(m):
        if a + apples[i] >= s and a + apples[i] <= t:
            x.append(k)

    for j in range(n):
        if b + oranges[j] >= s and b + oranges[j] <= t:
            y.append(k)

    x1 = len(x)
    y1 = len(y)

    return x1
    return y1

st = input().split()
st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)



