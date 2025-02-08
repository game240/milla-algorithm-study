def logic():
    global n, m, square

    # 가능한 정사각형의 최대 크기: min(n, m)
    # 큰 정사각형부터
    for size in range(min(n, m), 1, -1):
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                if square[i][j] == square[i][j + size - 1] and square[i][j + size - 1] == square[i + size - 1][j] and square[i + size - 1][j] == square[i + size - 1][j + size - 1]:
                    return size 
    # 없는 경우
    return 1

n, m = map(int, input().split())

square = []
for i in range(n):
    square.append(input())

print(logic() ** 2)     
