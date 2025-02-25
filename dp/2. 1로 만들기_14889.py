# 단순히 1~3 순서대로 해버리면 문제 발생. 10: 10 → 9 → 3 → 1
n = int(input())
# dp[i]: i까지의 최소 경우의 수
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1 # 3번 규칙
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])
