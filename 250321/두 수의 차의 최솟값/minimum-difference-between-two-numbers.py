n = int(input())

lista = list(map(int, input().split()))

lista.reverse()

result = lista[0]-lista[1]

for i in range(0, n-1):
    if lista[i]- lista[i+1] <=result:
        result = lista[i]- lista[i+1]

print(result)