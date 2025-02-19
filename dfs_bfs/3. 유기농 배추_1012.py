import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

m, n, k = 0, 0, 0
visited = []
field = []

# x, y: 탐색 시작 좌표
def dfs(x, y):
    if visited[y][x] == True:
        return

    visited[y][x] = True
    
    for i in range(4):
        dx = dir_x[i]
        dy = dir_y[i]

        if y + dy < 0 or y + dy > n - 1 or x + dx < 0 or x + dx > m - 1:
            continue
        
        if field[y + dy][x + dx] == 1 and visited[y + dy][x + dx] == False:
            dfs(x + dx, y + dy)
    
# ------------- main() -----------------    

t = int(input())

dir_x = [0, 0, -1, 1]
dir_y = [-1, 1, 0, 0]

count = 0
def run_test_cases():
    global count, m, n, k, visited, field
    m, n, k = map(int, input().split())

    visited = [[False for _ in range(m)] for _ in range(n)]

    # [[0, 0], [1, 0], ...]
    position_exists = []
    for i in range(k):
        position_exists.append(list(map(int, input().split())))
    
    field = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in position_exists:
        field[y][x] = 1

    for x, y in position_exists:
        if visited[y][x] == False:
            count += 1
            dfs(x, y)

for i in range(t):
    count = 0
    run_test_cases()
    print(count)
