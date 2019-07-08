from functools import reduce

i = 13
j = 45
k = 3
A=[]
for i in range(13,45+1):
    A.append(str(i))
print(A)
B = []
for j in A:
    str =''
    for k in j:
        str = k + str
    B.append(str)

print(B)
C = []
for l in range(len(B)):
    z = abs(int(A[l]) - int(B[l]))

    C.append(z)
print(C)
D = []
for m in range(len(C)):
    if int(C[m])% k == 0:
        D.append(C[m])

print(D)
print(len(D))
