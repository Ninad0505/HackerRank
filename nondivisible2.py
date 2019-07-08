counts = [10,6,1,3,4,5]
k = 6
count = min(counts[0], 1)
print(count)
for i in range(1, k//2+1):
    if i != k - i:
        count += max(counts[i], counts[k-i])
if k % 2 == 0:
    count += 1

print(count)
print(sum(counts))