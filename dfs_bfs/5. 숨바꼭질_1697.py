from collections import deque

n, k = map(int, input().split())
queue = deque()
# x - 1, x + 1, x * 2
dx = [-1, 1, 2]

visited = [False] * 100001

queue.append(n)
visited[n] = True
count = 0
flag = False
while queue:
    # len(queue): 이 때 정해지면 바뀌지 않음
    for i in range(len(queue)):
        # node 방문
        node = queue.popleft()
        if node == k:
            flag = True
            break
    
        for i in range(len(dx)):
            if i != 2:
                next_node = node + dx[i]
            else:
                next_node = node * dx[i]
    
            if next_node < 0 or next_node > 100001 - 1:
                continue
            
            if visited[next_node] == False:
                visited[next_node] = True
                queue.append(next_node)

    if flag == False:
        count += 1

print(count)
