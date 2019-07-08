nk = input().split()

n = int(nk[0])

k = int(nk[1])

a = list(map(int, input().rstrip().split()))

def angryProfessor(k, a):
    A = []
    for i in range(len(a)):
        if a[i] <= 0:
            A.append(a[i])

    if len(A) < k:
        print('Yes')


    else:
        print('No')

result = angryProfessor(k, a)