lista = list(map(int, input().split()))

cntList = [0,0,0,0,0,0,0,0,0,0]

for i in lista:
    if i==0:
        break
    else:
        if i==100:
            cntList[0]+=1
        elif (i//10%10)==0:
            continue
        else:
            cntList[10-(i//10%10)]+=1

c=100
for i in cntList:
    print(f'{c} - {i}')
    c-=10

