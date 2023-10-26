import math
from math import floor
a = str(input())
if (a == "W"):
    print("ติด ร")
else:
    b = str(input())
    c = str(input())
    d = str(input())
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    sum = a+b+c+d
    if (sum >= 80):
        grade = 4
    elif (sum >= 50):
        grade = (floor((sum-40)/5))/2
    else:
        grade = 0
    if (not(grade%1)):
        grade = int(grade)
    print(grade)