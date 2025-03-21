n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

result = 0

for i in range(0, len(price)):
    for j in range(i, len(price)):
        if ((price[i]-price[j])<=result):
            result = (price[i]-price[j])
print(-(result))
        