def returnM():
    metrix=[]
    for i in range(3):
        low = list(map(int,input().split()))
        metrix.append(low)
    return metrix

metrix1 = returnM()
dummy = input()
metrix2 = returnM()

newMetrix = []
for i in range(3):
    low = []
    for j in range(3):
        low.append(metrix1[i][j]*metrix2[i][j])
    newMetrix.append(low)

for i in range(3):
    for j in range(3):
        print(newMetrix[i][j],end=' ')
    print()

        