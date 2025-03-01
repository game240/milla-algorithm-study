import sys
input = sys.stdin.readline

n = int(input())

T = [0]
P = [0]
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# dp: i번째 날부터 N번째 날까지의 가장 높은 수익
dp = [0] * (n + 2)

# 역순으로 dp 계산
for i in range(n, 0, -1):
    if i + T[i] <= n + 1:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])
