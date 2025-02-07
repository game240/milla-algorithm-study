def not_gate(s):
    if s == 'W':
        return 'B'
    else: # s == 'B'
        return 'W'

def calc_count(x, y, first): # x, y: 8 * 8의 (0, 0) 좌표, first: (0, 0)의 시작 색상 값
    count = 0
    correct_next_row_start = first
    for i in range(x, x + 8):
        correct_next_alpha = correct_next_row_start
        for j in range(y, y + 8):
            # 맞는 색이 아닐 경우
            if board[i][j] != correct_next_alpha:
                count += 1
            correct_next_alpha = not_gate(correct_next_alpha)
            
        # 다음 줄 색 초기화
        correct_next_row_start = not_gate(correct_next_row_start)
    return count

n, m = map(int, input().split())

# m * n
board = []
for i in range(n):
    board.append(input())

# init
result = 64
# 0 <= i <= m - 8
for i in range(n - 7):
    for j in range(m - 7):
        # (0, 0)을 'W'로 시작하는 경우
        c1 = calc_count(i, j, 'W')
        # (0, 0)을 'B'로 시작하는 경우
        c2 = calc_count(i, j, 'B')
        result = min(result, c1, c2)

print(result)
