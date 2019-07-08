import math


def squares(a, b):

    A = []
    for i in range(a,b+1):
        a = math.sqrt(i) - int(math.sqrt(i))
        if a == 0:
            A.append(i)

    print(len(A))

result = squares(3, 9)


