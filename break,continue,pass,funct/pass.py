a = int(input())
b = int(input())
c = int(input())
ans = c
if (a > b and a > c):
    if (a > c):
        ans = a
elif (b > c and b > a):
        ans = b
else: pass
print(ans)

