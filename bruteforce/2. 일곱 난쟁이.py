def find_unknown(height):
    summation = sum(height)
    
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
    
            if summation - height[i] - height[j] == 100:
                # index return할 경우 pop 시에 index 꼬일 가능성 존재
                return height[i], height[j]

height = []
for i in range(9):
    height.append(int(input()))

a, b = find_unknown(height)
height.pop(height.index(a))
height.pop(height.index(b))
height.sort()

for i in height:
    print(i)
