aCnt = 0
bCnt = 0
cCnt = 0
dCnt = 0

for _ in range(3):
    state, fever = input().split()
    fever = int(fever)

    if state=='Y' and fever>=37:
        aCnt+=1
    elif state=='N' and fever>=37:
        bCnt+=1
    elif state=='Y' and fever<37:
        cCnt+=1
    elif state=='N' and fever<37:
        dCnt+=1

print(aCnt, bCnt, cCnt, dCnt, end=' ')
if aCnt>=2:
    print('E')


