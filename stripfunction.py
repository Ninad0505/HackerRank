a = list(map(int, input().rstrip().split()))
unique_list = []

for x in a:
    if x not in unique_list :
        unique_list.append(x)

unique = sorted(unique_list)

B = []
for j in range(len(unique)):
    A = []
    for i in range(len(a)):

        if unique[j] == a [i] :
            A.append(a[i])
    B.append(len(A))

#C = []
#for i in range(len(B)-1):
#    w = B[i] + B[i+1]
#    C.append(w)
C = []
for i in range (len(B)-1):
    if unique[i] - unique[i+1] == -1  :
        w = B[i] + B[i + 1]
        C.append(w)

if C == []:
    C.append(0)



print(len(a))
print(unique)
print(B)
print(C)

if max(C) > max(B):
    print(max(C))
else :
    print(max(B))