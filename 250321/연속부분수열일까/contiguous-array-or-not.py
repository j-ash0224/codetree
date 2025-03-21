n1, n2 = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

start=0
startAindex = -1

for i in range(n1):
    if A[i]==B[0]:
        start=1
        startAindex = i
        break

result = 'No'
cnt=0

if start==1:
    for i in range(startAindex, n1+1):
        if cnt==n2:
            break
        if A[i]==B[cnt]:
            cnt+=1
            result = 'Yes'
            continue
        else:
            result = 'No'
            break


print(result)

        
        



