def T(n):
    global T_cache
    
    if n in T_cache:
        return T_cache[n]
    else:
        T_cache[n] = n * (n + 1) // 2
        return T_cache[n]

def search(k, index):
    # 삼중 for문으로 T_n 탐색, 완전 종료 조건: T(a) <= k or T(b) <= k or T(c) <= k:
    for a in range(1, k):
        if T(a) > k:
            break
        for b in range(1, k):
            if T(b) > k:
                break
            for c in range(1, k):
                if T(c) > k:
                    break
                    
                if T(a) + T(b) + T(c) == k:
                    solved_list[index] = 1
                    return

n = int(input())

k_list = []
for i in range(n):
    k_list.append(int(input()))

# 해결됐는지 여부
solved_list = [0] * n
# T_n
T_cache = {}

# 모든 테스트 케이스 탐색
for i in range(len(k_list)):
    search(k_list[i], i)
    
for i in range(len(k_list)):
    print(solved_list[i])
