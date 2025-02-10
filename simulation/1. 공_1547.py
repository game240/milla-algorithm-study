m = int(input())
switch = []
for i in range(m):
    switch.append(list(map(int, input().split())))

cup = {i: 0 for i in range(1, 4)}
cup[1] = 1

for i in range(m):
    cup[switch[i][0]], cup[switch[i][1]] = cup[switch[i][1]], cup[switch[i][0]]

flag = False
for i in cup:
    if cup[i] == 1:
        print(i)
        flag = True

if flag == False:
    print(-1)
