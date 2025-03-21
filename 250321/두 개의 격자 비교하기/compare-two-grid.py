n, m = map(int, input().split())

def returnM(n):
    metrix=[]
    for i in range(n):
        low = list(map(int,input().split()))
        metrix.append(low)
    return metrix

metrix1 = returnM(n)
metrix2 = returnM(n)

for i in range(n):
    for j in range(n):
        if metrix1[i][j] == metrix2[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
    
