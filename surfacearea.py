HW = input().split()

H = int(HW[0])

W = int(HW[1])

A = []

for _ in range(H):
    A.append(list(map(int, input().rstrip().split())))


print(A)
print(H)
print(W)

B = []

one = H*W*2
B.append(one)

for i in range(H):
    for j in range(W):

        C = A[i+1][i] - A[i][i]

