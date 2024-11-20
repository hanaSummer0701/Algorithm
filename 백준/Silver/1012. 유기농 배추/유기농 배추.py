from collections import deque
t = int(input())

# 상하좌우 탐색
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a, b): # a,b = 탐색 시작 지점
    queue = deque()
    queue.append((a,b)) 
    graph[a][b] = 0 # 탐색 시작한 지점은 0으로 설정하여 재방문x

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)] # n*m 2차원 리스트 초기화, 값=0

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)