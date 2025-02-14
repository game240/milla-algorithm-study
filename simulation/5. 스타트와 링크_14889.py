# 팀원들의 총 능력치 계산
# teammates: 같은 팀원들 번호. e.g. [1, 2, 3]
def calculate_ability(S, teammates):
    total = 0
    # 11(0) + 12 + 13, 21 + 22(0) + 23, 31 + 32 + 33(0)
    for i in range(len(teammates)):
        for j in range(len(teammates)):
            total += S[teammates[i]][teammates[j]]
            
    return total

def dfs(start):
    global selected, min_diff
    
    if selected.count(True) == n // 2:
        start_team = []
        link_team = []
        for i in range(1, n + 1):
            if selected[i]:
                start_team.append(i)
            else:
                link_team.append(i)
                
        start_score = calculate_ability(S, start_team)
        link_score = calculate_ability(S, link_team)
        min_diff = min(min_diff, abs(start_score - link_score))
        return

    # iteration으로 dfs 시행
    for i in range(start, n + 1):
        if not selected[i]:
            # i번째를 start 팀에 포함시켜서 진행
            selected[i] = True
            dfs(i + 1)
            # 초기화 
            selected[i] = False

# ----------------------- main -----------------------------
n = int(input())

# index 1부터 시작
S = [[0] * (n + 1)]
for i in range(n):
    row = list(map(int, input().split()))
    S.append([0] + row)

# selected: start 팀에 들어가는지 여부 (True면 Start, False면 Link)
selected = [False] * (n + 1)
min_diff = float('inf')

dfs(1)
print(min_diff)
