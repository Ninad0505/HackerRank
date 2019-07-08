n = int(input())

container = []

for _ in range(n):
    container.append(list(map(int, input().rstrip().split())))

print(container)

A = []

for i in range (n):
    a = 0
    for j in range (n):
        a = a + container[j][i]
    A.append(a)

A.sort()
B = []
for i in range (n):
    b = 0

    for j in range(n):
        b = b + container[i][j]
    B.append(b)
B.sort()
if A != B:
    print('n')
print(A)
print(B)
