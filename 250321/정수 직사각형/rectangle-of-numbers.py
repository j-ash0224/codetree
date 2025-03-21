n , m = map(int, input().split())

num = 1

metrix = []

for i in range(n):
    low = []
    for j in range(m):
        low.append(num)
        num+=1
    metrix.append(low)

for i in range(n):
    for j in range(m):
        print(metrix[i][j], end=' ')
    print()
