
n = int(input())

s = input()
B = s[4]
print(B)
print(type(B))
A = [0]
C = []
for j in s:
    if j == 'U':
        A[-1] = A[-1] + 1
        A.append(A[-1])

    elif j == 'D':
        A[-1] = A[-1] - 1
        A.append(A[-1])

print(A)
for k in range(len(A)):
    z = 1
    if A[k] == -1 and A[k + 1] == 0:
        C.append(z)

print(C)