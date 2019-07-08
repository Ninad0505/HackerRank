x1 = int(input('enter k1 posi'))
v1 = int(input('k1 velo'))
x2 = int(input('enter k2 posi'))
v2 = int(input('k2 velo'))

A = []
B = []
i = 0

while i<50:
    a = x1 + i
    A.append(a)
    i = i + v1
k=0
while k<20:
    b = x2 + k
    B.append(b)
    k = k + v2


if len(A)>len(B):
    n = len(B)
else :
    n = len(A)
for j in range(n):
    if A[j]==B[j]:
        print('yes')
        break
else :
    print('no')



print(A)
print(B)