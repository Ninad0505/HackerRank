

list = [1,2,3,4,5,6,7,8,9,10,12,30]
n = [4,12,30]

for i in range(len(n)):
    l=0
    u=len(list) - 1

    while l<=u:


        mid = (l+u) // 2
        if list[mid]==n[i]:

            print(mid + 1)
            break

        else :
            if list[mid]<n[i]:
                l=mid + 1

            else :
                u = mid - 1


