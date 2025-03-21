n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

def findMaxNum(li):
    maxX = max(li)

    newList = []

    for i in range(0, len(li)):
        if li[i]==maxX:
            print(i+1, end=' ')
            break
        else:
            newList.append(li[i])

    if newList!=[]:
        findMaxNum(newList)

findMaxNum(a);


    
    