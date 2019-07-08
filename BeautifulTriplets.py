nd = input().split()

n = int(nd[0])

d = int(nd[1])

arr = list(map(int, input().rstrip().split()))

def beautifulTriplets(d, arr):
    gc = 0
    for i in range(n):
        if arr[i] + d in arr and arr[i] + 2 * d in arr:
            gc += 1
    print(gc)

result = beautifulTriplets(d, arr)



