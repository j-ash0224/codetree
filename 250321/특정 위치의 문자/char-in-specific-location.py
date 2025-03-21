idx = -1

list = ['L','E','B','R','O','S',]

a = input()

for i in range(6):
    if a==list[i]:
        print(i)
        idx = i

if idx == -1:
    print('None')