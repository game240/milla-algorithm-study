n = int(input())

result = 0
for i in range(1, n):
    # init
    s = 0
    
    for j in str(i):
        s += int(j)
    if i + s == n:
        result = i
        break
    
print(result)
