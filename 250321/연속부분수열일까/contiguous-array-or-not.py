n1, n2 = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
        
listCount = n1-n2+1
result = 'No'

for i in range(0, listCount):
    checkList=[]
    cnt = i
    for _ in range(n2):
        checkList.append(A[cnt])
        cnt+=1
    if checkList==B:
        result='Yes'
        break

print(result)
