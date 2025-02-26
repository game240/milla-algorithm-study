def fibo(n):
    global dp
    
    if n == 0 or n == 1:
        return dp[n]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
print(fibo(n) % 10007)
