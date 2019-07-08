
bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

def getMoneySpent(keyboards, drives, b):

    A = [-1]
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            z = keyboards[i] + drives[j]
            if z <= b :
                A.append(z)


    print(max(A))

moneySpent = getMoneySpent(keyboards, drives, b)

