n = int(input())

alist = list(map(int, input().split()))



    
for j in range(1,10):
    cnt=0
    for i in alist:
        if j==i:
            cnt+=1
    print(cnt)
