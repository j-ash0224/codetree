listA = list(map(int, input().split()))

newList = []

for i in listA:
    if (i == 999) or (i==-999):
        break
    else:
        newList.append(i)

print(max(newList), min(newList))
