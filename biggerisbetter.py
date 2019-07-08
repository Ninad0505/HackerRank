string = 'dkhc'
A = []
for i in range(len(string)):
    A.append(string[i])
for i in range(len(string)):
    try :
        if string[-1-i] > string[-2-i]:
            n = -1 - i
            print(n)
            break

    except Exception :
        n = - len(string)

if n == - len(string):
    print('no answer')

else :
    print(A)

    B = []
    if ord(A[n-1]) < ord(A[-1]):
        B.append(A[-1])
        B.append(A[n-1])
        for z in range(-n -1):
            B.append(A[-2-z])

        print(B)

        answer = ''
        for x in range(len(string) - 1 + n):
            answer += A[x]

        for y in range(len(B)):
            answer += B[y]

    else :
        for q in range(len(A)):
            if ord(A[n - 1]) > ord(A[-1-q]):

                N = -1-q
                break

        B.append(A[N])
        for w in range(-N-1):
            B.append(A[-1-w])
        B.append(A[n-1])

        for t in range(N-1,n-1):
            B.append(A[t])

        print(B)

        answer = ''
        for x in range(len(string) - 1 + n):
            answer += A[x]
        for y in range(len(B)):
            answer += B[y]




    print(answer)

