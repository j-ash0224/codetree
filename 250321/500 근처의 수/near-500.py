alist = list(map(int,input().split()))

minX = 1000
maxX = 0

for i in alist:
    if i<500 and i>=maxX:
        maxX = i
    if i>500 and i<=minX:
        minX = i

print(maxX, minX)