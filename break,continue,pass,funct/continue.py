sum = 0
for i in range(10):
    x = int(input())
    if (x < 0):
        continue
    sum += x
print(sum)