lista = list(map(int, input().split()))

cntList = [0,0,0,0,0,0,0,0,0]

for i in lista:
    if i==0:
        break
    else:
        if (i//10%10)==0:
            continue
        else:
            cntList[(i//10%10)-1]+=1

c=1
for i in cntList:
    print(f'{c} - {i}')
    c+=1

