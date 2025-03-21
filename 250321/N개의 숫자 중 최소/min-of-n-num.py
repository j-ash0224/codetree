n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

x = min(a)

print(x, a.count(x), sep=' ')
