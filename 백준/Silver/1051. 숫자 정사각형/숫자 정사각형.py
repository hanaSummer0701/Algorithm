# N/M
n, m = map(int, input().split())

# 직사각형을 입력받아 리스트에 저장
square=[]
for _ in range(n):
        square.append(list(map(int, (input())))) 

# 가능한 정사각형의 최대 길이
max_s = min(n, m)

# 네 꼭짓점의 숫자가 모두 같은 경우
# 가능한 정사각형의 시작 위치 구하기 -> +1은 정사각형 끝 범위를 넘지 않도록 하기 위함.
def same_num(s): # s: s*s크기의 정사각형 정의
    for i in range(n-s+1):
        for j in range(m-s+1):
            if square[i][j] == square[i][j+s-1] == square[i+s-1][j] == square[i+s-1][j+s-1]:
                return True
    return False

# 최대부터 -1씩 작아지며 일치하는 경우 찾기
# max_s부터 -1하며 0까지 반복
for k in range(max_s, 0, -1):
    if same_num(k):
        print(k**2) # 변의 길이의 제곱 출력 -> 정사각형이기 때문
        break