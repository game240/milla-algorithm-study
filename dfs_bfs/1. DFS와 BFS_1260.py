from collections import deque

def dfs(v):
    global graph, visited

    visited[v] = True
    print(v, end = " ")

    for i in range(len(graph[v])):
        if visited[graph[v][i]] == False:
            dfs(graph[v][i])
        
def bfs(v):
    global graph, visited
    queue = deque([v])
    visited[v] = True

    while queue:
        # queue의 첫번째 node 탐색
        node = queue.popleft()
        print(node, end = " ")
        
        # target: each nodes
        for target in graph[node]:
            if visited[target] == False:
                queue.append(target)
                visited[target] = True

n, m, v = map(int, input().split())

# [[1, 2], [1, 3], ...]
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

# {1: [2, 3], ...}
graph = {i: [] for i in range(1, n + 1)}
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

# 작은 것을 먼저 방문
for node in graph:
    graph[node].sort()

# node 번호: 1부터 시작
visited = [False] * (n + 1)
dfs(v)
print()

visited = [False] * (n + 1)
bfs(v)
