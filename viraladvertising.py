
n = 5
A = [5]
a = 5
for i in range (1,n):
    b = a // 2
    b = b*3
    a = b
    A.append(a)

print(A)
B = list(map(lambda n : n//2, A))
print(B)

