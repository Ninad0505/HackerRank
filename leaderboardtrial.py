scores =[100,90,90,80,75,60]

alice = [50,65,77,90,102]
alice_count = 5
def climbingLeaderboard(scores, alice):


    for i in range(alice_count):
        scores.append(alice[i])
        unique = []
        for x in scores:
            if x not in unique:
                unique.append(x)

        sscores = sorted(unique, reverse = True)
#        for j in range(len(sscores)):
#           if sscores[j] == alice[i]:
#               P = str(j+1)
#               print(P)

        l = 0
        u = len(sscores) - 1
        while l<=u :
            mid = (l + u) // 2
            if sscores[mid] == alice[i]:

                print(mid + 1)
                break

            else:
                if sscores[mid] < alice[i]:
                    l = mid + 1

                else:
                    u = mid - 1











climbingLeaderboard(scores, alice)