each_count = 0

def dfs(x, y):
    global visited, each_counted, n, each_count, maps
    if visited[y][x] == True:
        return
    
    visited[y][x] = True
    if each_counted[y][x] == False:
        each_counted[y][x] = True
        each_count += 1

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        # 범위: 0 to n - 1
        if x + dx[i] < 0 or x + dx[i] > n - 1 or y + dy[i] < 0 or y + dy[i] > n - 1:
            continue

        if maps[y + dy[i]][x + dx[i]] == 1 and visited[y + dy[i]][x + dx[i]] == False:
            dfs(x + dx[i], y + dy[i])

n = int(input())

maps = []
for i in range(n):
    maps_row = []
    temp = input()
    for position in temp:
        maps_row.append(int(position))
    maps.append(maps_row)

visited = [[False for _ in range(n)] for _ in range(n)]
each_counted = [[False for _ in range(n)] for _ in range(n)]

each_count_list = []
total_count = 0
for i in range(n): # y축
    for j in range(n): # x축
        if maps[i][j] == 1 and visited[i][j] == False:
            # 하나의 섹션에선 해당 호출로 전부 끝남
            dfs(j, i)
            total_count += 1
            each_count_list.append(each_count)
            # init
            each_count = 0

each_count_list.sort()
print(total_count)
for i in each_count_list:
    print(i)
