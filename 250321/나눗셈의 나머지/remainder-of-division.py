a, b = map(int,input().split())

listA = [0,0,0,0,0,0,0,0,0]

while(a>1):
    listA[(a%b)]+=1
    a = a//b

sum = 0

for i in listA:
    sum+=i**2
print(sum)