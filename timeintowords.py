alice = [50,65,77,90,102]
scores = [100,90,90,80,75,60]


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