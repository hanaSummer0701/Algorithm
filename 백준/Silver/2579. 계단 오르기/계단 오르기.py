n = int(input())
stair = [0] + [int(input()) for _ in range(n)]  # 1-based indexing

dp_s = [0] * (n + 1)

# 초기값 설정
if n == 1:
    dp_s[1] = stair[1]
elif n == 2:
    dp_s[1] = stair[1]
    dp_s[2] = stair[1] + stair[2]
else:
    dp_s[1] = stair[1]
    dp_s[2] = stair[1] + stair[2]

    # 점화식 적용
    for i in range(3, n + 1):
        dp_s[i] = max(dp_s[i - 3] + stair[i - 1] + stair[i], dp_s[i - 2] + stair[i])

print(dp_s[n])
