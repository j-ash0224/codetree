n, q = map(int,input().split())

lista = list(map(int,input().split()))

for _ in range(q):
    qureyList = list(map(int,input().split()))

    if qureyList[0] ==1:
        print(lista[qureyList[1]-1])
    elif qureyList[0] ==2:
        for i in range(n):
            if lista[i] == qureyList[1]:
                print(i+1)
                break
    elif qureyList[0] ==3:
        for i in range(qureyList[1], qureyList[2]+1):
            print(lista[i-1], end=' ')
        print()
        