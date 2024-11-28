# 12026

n = int(input())
block = list(input())
dp_b = [float('inf')] * n  # 초기값을 무한대로 설정
dp_b[0] = 0  # 시작점은 에너지 0

def jump(i):
    if i == 'B':
        return  'O'
    elif i == 'O':
        return 'J'
    elif i == 'J':
        return 'B'
    
# 점화식 적용
for k in range(n):
    for j in range(k+1, n):
        if block[j] == jump(block[k]):
            dp_b[j] = min(dp_b[j], dp_b[k]+(j-k)**2)

if dp_b[n-1] != float('inf'):
    print(dp_b[n-1])
else:
    print(-1)
