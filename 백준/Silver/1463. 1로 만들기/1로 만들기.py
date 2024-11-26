# 1463
n = int(input())

# dp 테이블 초기화
dp = [0]*(n+1)

# bottom-up
def bottom_up(i):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    return dp[i]

for k in range(2, n+1):
    bottom_up(k)
print(dp[n])