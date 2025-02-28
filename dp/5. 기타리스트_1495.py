result_list = []

def dfs(i, current_volume):
    global n, m, V, visited

    # 다 돌았을 경우
    if i == n:
        result_list.append(current_volume)
        return

    if visited[i][current_volume]:
        return
    visited[i][current_volume] = True
    
    if current_volume + V[i] <= m:
        dfs(i + 1, current_volume + V[i])
    if current_volume - V[i] >= 0:
        dfs(i + 1, current_volume - V[i])


n, s, m = map(int, input().split())
V = list(map(int, input().split()))

current_volume = s
visited = [[False] * (m + 1) for _ in range(n + 1)]
dfs(0, s)

if not result_list:
    print(-1)
else:
    print(max(result_list))
