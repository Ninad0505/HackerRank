t = int(input())

    for t_itr in range(t):
        n = int(input())
def utopianTree(n):
    height = [1]

    for i in range(60):
        if i%2 == 0:
            z = height[-1]*2

            height.append(z)
        else :
            y = height[-1] + 1
            height.append(y)

    HEIGHT = height[n]
    print(HEIGHT)

result = utopianTree(n)