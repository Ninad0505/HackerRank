nk = input().split()

n = int(nk[0])

k = int(nk[1])

r_qC_q = input().split()

r_q = int(r_qC_q[0])

c_q = int(r_qC_q[1])

obstacles = []

for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))


print(obstacles)


max = max(r_q, c_q)
A = []
C = []
for i in range(3):
    if obstacles[i][0] == r_q:
        A.append(obstacles[i][1] )

B = []
for j in range(3):
    if obstacles[j][1] == c_q:
        B.append(obstacles[j][0])
Z = []
z = 1
if r_q + c_q < n+1:
    if c_q > r_q :
        for i in obstacles:
            for j in range(n - c_q):
                if i != [r_q + j+1, c_q +j+1]:
                    Z.append(z)

        for i in obstacles:
            for j in range(r_q - 1):
                if i != [r_q - (j+1), c_q + (j+1)]:
                    Z.append(z)

        for i in obstacles:
            for j in range(c_q - 1):
                if i != [r_q + (j+1), c_q - (j+1)]:
                    Z.append(z)

        for i in obstacles:
            for j in range(r_q - 1):
                if i != [r_q - (j+1), c_q - (j+1)]:
                    Z.append(z)

elif r_q + c_q == n +1 :

    for i in obstacles:
        for j in range(n - c_q):
            if i != [r_q - (j+1), c_q + (j+1)]:
                Z.append(z)

    for i in obstacles:
        for j in range(n - max):
            if i != [r_q + (j+1), c_q + (j+1)]:
                Z.append(z)

    for i in obstacles:
        for j in range(n - r_q):
            if i != [r_q + (j+1), c_q - (j+1)]:
                Z.append(z)

    for i in obstacles:
        for j in range(n - max):
            if i != [r_q - (j+1), c_q - (j+1)]:
                Z.append(z)








print(A)
print(B)
print(C)