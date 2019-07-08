q = int(input())

for q_itr in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])


def catAndMouse(x, y, z):
    for q_itr in range(q):
        A = abs ( z - x)
        B = abs ( z - y)
        if A == B :
            print ( 'Mouse C')

        elif A > B:
            print ( 'Cat B')

        else :
            print('Cat A')


result = catAndMouse(x, y, z)