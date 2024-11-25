# 2748
n=int(input())

def fibo(n, memo={}):
    # 계산한 적 있는 경우
    if n in memo:
        return memo[n]
    if n==1 or n==2:
        return 1
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]
print(fibo(n))