#1018

# 다시 칠해야 하는 경우 맨 왼쪽위 흰색, 검은색
m, n = map(int, input().split())

# 리스트 정의
board=[]
chess=[]

# 전체 체스판을 리스트에 저장
for _ in range(m):
    board.append(input())

# 가로, 세로 길이가 8이면 1번만 반복문 돌게 설정
for i in range(m-7):
    for j in range(n-7):
        w_tile, b_tile = 0, 0
        for w in range(i, i+8):
            for b in range(j, j+8):
                if (w+b)%2 == 0:
                    if board [w][b] != 'W':
                        w_tile+=1
                    if board [w][b] != 'B':
                        b_tile+=1
                else:
                    if board [w][b] !='B':
                        w_tile+=1
                    if board [w][b] !='W':
                        b_tile+=1
        chess.append(w_tile)
        chess.append(b_tile)
print(min(chess))