# 1697
from collections import deque

n, k = map(int, input().split())
def bfs(n, k):
    visited = [False] * 100001
    queue = deque([(n,0)])
    visited[n] = 0
    find_count=0

    
    while queue:
        x, time = queue.popleft()
        if x == k:
            if visited[k] == time:
                find_count += 1
            continue
        # 가능한 이동 거리
        for move in [x-1, x+1, x*2]:
            if 0 <= move <= 100000:
                if visited[move] == False or visited[move]== time + 1:
                    visited[move] = time + 1
                    queue.append((move, time+1))
    return visited[k], find_count
                
min_time, count_way = bfs(n,k)
print(min_time)
print(count_way)
