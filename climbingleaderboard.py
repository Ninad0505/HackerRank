scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))


def climbingLeaderboard(scores, alice):
    for i in range(len(alice)):
        scores.append(alice[i])
        unique = []
        for x in scores:
            if x not in unique:
                unique.append(x)
        unique.sort(reverse=True)

        l = 0
        u = len(unique) - 1

        while l <= u:
            mid = (l + u) // 2
            if unique[mid] == alice[i]:
                print(unique)
                print(mid + 1)
                break
            else:
                if unique[mid] > alice[i]:
                    l = mid + 1
                else:
                    u = mid - 1
        scores.remove(alice[i])











climbingLeaderboard(scores, alice)