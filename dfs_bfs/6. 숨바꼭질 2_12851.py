from collections import deque

n, k = map(int, input().split())
queue = deque()
dx = [-1, 1, 2]

# 각 위치까지 도달하는 최소 시간을 저장 (-1: 아직 방문 안함)
visited = [-1] * 100001
# 각 위치까지 최단 시간으로 도달하는 방법의 수
count = [0] * 100001

queue.append(n)
visited[n] = 0
count[n] = 1

time = 0
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        for i in range(3):
            if i != 2:
                next_node = node + dx[i]
            else:
                next_node = node * dx[i]
            
            if next_node < 0 or next_node > 100000:
                continue
            
            # 처음 방문한 경우: 최소 시간 갱신 및 경로 수 초기화
            if visited[next_node] == -1:
                visited[next_node] = time + 1
                count[next_node] = count[node]
                queue.append(next_node)
            # 이미 같은 최단 시간에 도달한 경우: 경로 수 누적
            elif visited[next_node] == time + 1:
                count[next_node] += count[node]
    
    time += 1
    # 만약 k에 도달한 최소 시간이 기록되었고, 현재 time이 그보다 커지면 종료
    if visited[k] != -1 and time > visited[k]:
        break

print(visited[k])
print(count[k])
