n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
newLsit = []

for i in nums:
    if nums.count(i)>=2:
        continue
    else:
        newLsit.append(i)

if newLsit !=[]:
    print(max(newLsit))
else:
    print(-1)