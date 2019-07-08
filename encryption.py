import math

s ='haveaniceday'
l = int(math.sqrt(len(s))) + 1
A = []
i = 0
while i <= len(s):
    a = s[i:i+l]
    A.append(a)
    i = i + l


print(A)

list = []
for i in range(len(A[0])):

    list.append([])
    for j in range(len(A[0])):
        if j < len(A[j]):
            break
            z = A[j][i]
            list[j].append(z)

print(list)
