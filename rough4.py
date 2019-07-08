A = [8,8,14,10,3,5,14,12]

for i in range(len(A)):
    B = min(A)
    for i in range(len(A)):

        A[i] = A[i] - B

    A = list( filter( lambda n : n > 0, A))

    print(A)
    print(len(A))
