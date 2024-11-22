# 1697
from collections import deque

n, k = map(int, input().split())

def bfs(n, k):
    visited = [False] * 100001
    queue = deque([(n,0)])
    visited[n] = True

    while queue:
        x, time = queue.popleft()
        if x == k:
            return time
        # 가능한 이동 거리
        for move in [x-1, x+1, x*2]:
            if 0 <= move <= 100000 and not visited[move]:
                visited[move] = True
                queue.append((move, time+1))
print(bfs(n, k))
