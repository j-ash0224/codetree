n = int(input())

metrix = []

for i in range(n):
    low = []
    for j in range(n):
        low.append(0)
    metrix.append(low)


cnt =1

for j in range(n):
    for i in range(n):
        metrix[i][j] = cnt
        cnt+=1

for i in range(n):
    for j in range(n):
        print(metrix[i][j], end=' ')
    print()


