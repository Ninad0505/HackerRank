n = 5
m = 2
s = 2




if s + m < n:
    print(s + m - 1)
else:
    if (s+m - 1) % n == 0:
        print(n)
    else:
        print((s+m - 1) % n)