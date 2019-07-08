RC = input().split()

R = int(RC[0])

C = int(RC[1])

G = []

for _ in range(R):
    G_item = input()
    G.append(G_item)

rc = input().split()

r = int(rc[0])

c = int(rc[1])

P = []

for _ in range(r):
    P_item = input()
    P.append(P_item)


print(G)
print(P)

A = []

for j in range(len(G) - 1):
    if P[0] in G[j] and P[1] in G[j+1] :
        A.append(j)





for j in A:
    B = []
    for i in range(len(P)):
        if P[i] in G[j+i]:
            B.append(1)
    if len(B) == len(P):

        print('YES')
        break

else :
    print('NO')






