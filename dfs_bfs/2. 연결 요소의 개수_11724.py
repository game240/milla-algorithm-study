import sys
sys.setrecursionlimit(10 ** 6) 
input = sys.stdin.readline

def dfs(v):
    global graph, visited
    
    visited[v] = True
    
    for node in graph[v]:
        if visited[node] == False:
            dfs(node)

n, m = map(int, input().split())

# [[5, 1], ...]
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

graph = {i: [] for i in range(1, n + 1)}
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


visited = [False] * (n + 1)

count = 0
for i in range(1, n + 1):
    if visited[i] != True:
        dfs(i)
        count += 1

print(count)
