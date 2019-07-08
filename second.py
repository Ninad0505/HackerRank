import math
import os
import random
import re
import sys
from functools import reduce

def formingMagicSquare(s):

    a = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    b = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    c = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    d = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    e = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    f = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    g = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    h = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]

    diff = []

    A = []
    for i in range(3):
        for j in range(3):
            x = s[j][i] - a[j][i]
            A.append(abs(x))
    A1 = reduce(lambda p, q: p + q, A)
    diff.append(A1)

    B = []
    for i in range(3):
        for j in range(3):
            x = s[j][i] - a[j][i]
            B.append(abs(x))
    B1 = reduce(lambda p, q: p + q, A)
    diff.append(B1)

    C = []
    for i in range(3):
        for j in range(3):
            x = s[j][i] - a[j][i]
            C.append(abs(x))
    C1 = reduce(lambda p, q: p + q, A)
    diff.append(C1)

    D = []
    for i in range(3):
        for j in range(3):
            x = s[j][i] - a[j][i]
            D.append(abs(x))
    D1 = reduce(lambda p, q: p + q, A)
    diff.append(D1)

    E = []
    for i in range(3):
        for j in range(3):
            x = s[j][i] - a[j][i]
            E.append(abs(x))
    E1 = reduce(lambda p, q: p + q, A)
    diff.append(E1)

    F = []
    for i in range(3):
        for j in range(3):
            x = s[j][i] - a[j][i]
            F.append(abs(x))
    F1 = reduce(lambda p, q: p + q, A)
    diff.append(F1)

    G = []
    for i in range(3):
        for j in range(3):
            x = s[j][i] - a[j][i]
            G.append(abs(x))
    G1 = reduce(lambda p, q: p + q, A)
    diff.append(G1)

    H = []
    for i in range(3):
        for j in range(3):
            x = s[j][i] - a[j][i]
            H.append(abs(x))
    H1 = reduce(lambda p, q: p + q, A)
    diff.append(H1)

    print(min(diff))


s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)
