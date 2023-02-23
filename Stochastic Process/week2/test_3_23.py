from random import *
max = 100
n = 1000000
ans = 0.0
p = 0.5
list = []
for j in range(n):
    for i in range(max):
        temp = random()
        # print(temp)
        if(temp < p):
            list.append(1)
        else:
            list.append(0)
        if i == 1 and list[1] + list[0] == 2:
            ans+=(i+1)
            break
        elif i>=2 and list[i] + list[i-1] + list[i-2] >= 2:
            ans+=(i+1)
            break
    # print(list)
    list = []

print(ans / n)
