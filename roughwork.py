scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))

pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False


def climbingLeaderboard(scores, alice):
    pos = -1
    def search(list,n):
        l=0
        u=len(list)-1
        while l<=u:
            mid = (l+u)//2
            if list[mid]==n:
                globals()['pos']=mid
                return True
            else :
                if list[mid]<n :
                    l = mid + 1
                else :
                    u = mid - 1

        return False


    unique = []
    for x in scores:
        if x not in unique :
            unique.append(x)
    unique.sort(reverse = True)
    for i in range(len(alice)):
#       if alice[i] < min(unique):
#           print(len(unique) + 1)

        if search(unique, alice[i]):
            print(pos + 1)



    print(unique)



climbingLeaderboard(scores, alice)

