lista = []

for i in range(2):
    low = list(map(int,input().split()))
    lista.append(low)

for i in lista:
    ave = sum(i)/len(i)
    print(f'{ave:.1f}',end=' ')
print()

for j in range(4):
    sum = 0
    for i in range(2):
        sum+=lista[i][j]
    ave = sum/2
    print(f'{ave:.1f}',end=' ')
print()

sum = 0
for i in range(2):
    for j in range(4):
        sum+=lista[i][j]
ave = sum/8
print(f'{ave:.1f}',end=' ')

