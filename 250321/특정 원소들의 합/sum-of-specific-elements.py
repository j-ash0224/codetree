metrix = []

for i in range(4):
    low = list(map(int,input().split()))
    metrix.append(low)



sum = 0

for i in range(4):
    for j in range(4):
        if i>=j:
            sum+=metrix[i][j]

print(sum)

