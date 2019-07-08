from numpy import *

arr1 = array([
            [1,0,4],
            [2,3,4],
            [2,1,3]
])
arr2 = array([
            [2,2,4],
            [2,6,0],
            [2,1,0]
])
A = []
for k in range (3):

    for j in range (3):

        for i in range (3):
            x = arr1[k][i]*arr2[i][j]
            A.append(x)
print(A)
B=[]
l = 1
while l<len(A):
    y = A[l-1]+A[l]+A[l+1]
    B.append(y)
    l=l+3
print(B)
C = matrix(B)
D = C.reshape(3,3)
print(D)


m1 = matrix(arr1)
m2 = matrix(arr2)
mtheo = m1*m2
print(mtheo)
