def dfs(i, current, plus, minus, multiply, divide):
    global n, A, max_val, min_val
    # 모든 숫자를 사용했다면 결과값 갱신
    if i == n:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return

    next_num = A[i]
    # 덧셈 연산자 
    if plus:
        dfs(i + 1, current + next_num, plus - 1, minus, multiply, divide)
    # 뺄셈 연산자 
    if minus:
        dfs(i + 1, current - next_num, plus, minus - 1, multiply, divide)
    # 곱셈 연산자 
    if multiply:
        dfs(i + 1, current * next_num, plus, minus, multiply - 1, divide)
    # 나눗셈 연산자 사용 가능할 경우
    if divide:
        if current < 0:
            # 음수를 양수로 나눌 때, 먼저 절댓값으로 나눈 뒤 음수로 변환
            dfs(i + 1, -(-current // next_num), plus, minus, multiply, divide - 1)
        else:
            dfs(i + 1, current // next_num, plus, minus, multiply, divide - 1)

n = int(input())
A = list(map(int, input().split()))
operations = list(map(int, input().split()))

max_val = -10**9
min_val = 10**9

dfs(1, A[0], operations[0], operations[1], operations[2], operations[3])
print(max_val)
print(min_val)
