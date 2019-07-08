A = ['12345','29731','81836','12893','34923']
B = ['34','73','83']
C = []
for i in range(5):
    for j in range(4):
        if A[i][j] == '3' and A[i][j+1] == '4' :
            z = [i,j]
            C.extend(z)

for o in range(0,len(C),2):
    for j in range(2):
        for k in range(2):
            q = int(C[0 + o]) + j
            w = int(C[1 + o]) + k
            if B[j][k] == A[q][w]:
                print('yes')

print(C)
print(A[0][2])
print(A[0][3])
