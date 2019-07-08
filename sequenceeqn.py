n = int(input())
p = list(map(int, input().rstrip().split()))

def permutationEquation(p):
    A = []
    for i in range(1,n+1):
        for j in range(n):
            if i == p[j] :
                A.append(j+1)
    print(A)
    for k in range(n):
        for l in range(n):
            if p[l] == A[k] :
                print(str(l + 1))

result = permutationEquation(p)