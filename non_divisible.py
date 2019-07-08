numbers = [1,2,7,4]
k = 3


counts = [0] * k
for number in numbers:
    counts[number % k] += 1
    print(counts)

print(counts)

count = min(counts[0], 1)
print(count)
for i in range(1, k//2+1):
    if i != k - i:
        count += max(counts[i], counts[k-i])
if k % 2 == 0:
    count += 1

print(count)
