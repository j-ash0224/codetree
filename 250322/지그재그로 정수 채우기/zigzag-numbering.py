n, m = map(int, input().split())

# Please write your code here.


metrix = []
for i in range(n):
    low=[]
    for j in range(m):
        low.append(0)
    metrix.append(low)


cnt = 0

for j in range(m):
    for i in range(n):
        if j%2==0:
            metrix[i][j] = cnt
            cnt+=1
        elif j%2!=0:
            metrix[(n-1)-i][j] = cnt
            cnt+=1


for i in range(n):
    for j in range(m):
        print(metrix[i][j], end=' ')
    print()
            
