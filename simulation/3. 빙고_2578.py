def check_horizontal(x, y):
    global board_called
    
    for hor in range(5):
        # 하나라도 False면 0
        if board_called[y][hor] == False:
            return 0
    return 1

def check_vertical(x, y):
    global board_called
    
    for ver in range(5):
        # 하나라도 False면 0
        if board_called[ver][x] == False:
            return 0
    return 1

# (0, 0) ~ (4, 4)
def check_diagonal_1():
    global board_called

    for i in range(5):
        if board_called[i][i] == False:
            return 0
    return 1
            
# (4, 0), (3, 1), (1, 3), (0, 4)
def check_diagonal_2():
    global board_called

    for i in range(5):
        if board_called[4 - i][i] == False:
            return 0
    return 1   

def check_diagonal():
    return check_diagonal_1() + check_diagonal_2()
    
def check_bingo():
    # 각자 경우의 수들
    count = 0
    # row를 다르게 하여 x축 검사
    for row in range(5):
        count += check_horizontal(0, row)
    # column을 다르게 하여 y축 검사
    for col in range(5):
        count += check_vertical(col, 0)

    count += check_diagonal_1()
    count += check_diagonal_2()
    return count

def find_location(number):
    global board
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                # x, y 순서
                return j, i

def logic():
    global call, board_called
    for i in range(5):
        for j in range(5):
            x, y = find_location(call[i][j])
            # 지워짐 처리
            board_called[y][x] = True
            if check_bingo() >= 3:
                # index 0부터 시작
                return j + i * 5 + 1

board = []
for i in range(5):
    board.append(list(map(int, input().split())))
board_called = [[False for i in range(5)] for i in range(5)]

call = []
for i in range(5):
    call.append(list(map(int, input().split())))

print(logic())
