def calc_rank(a, b):
    if a == b:
        # 1땡: 101, ..., 장땡: 110
        return 100 + a
    else:
        # 0끗: 000, ..., 9끗: 009
        return (a + b) % 10

a, b = map(int, input().split())

deck = {i: 2 for i in range(1,11)}
deck[a] -= 1
deck[b] -= 1

my_rank = calc_rank(a, b)

total_cases = 0
win_cases = 0
for i in range(1, 11):
    for j in range(1, 11):
        # i == j이지만 같은 카드가 두 장 이상 없을 경우
        if i == j and deck[i] < 2:
            continue

        opposite_rank = calc_rank(i, j)
        if i == j:
            cases = deck[i] * (deck[i] - 1) # 같은 카드를 두장 가져가는 경우의 수
        else:
            cases = deck[i] * deck[j] # 다른 카드를 하나씩 가져가는 경우의 수

        total_cases += cases
        if my_rank > opposite_rank:
            win_cases += cases

print(f"{win_cases / total_cases:.3f}")
