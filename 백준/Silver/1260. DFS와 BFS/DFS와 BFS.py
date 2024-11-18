from collections import deque

# 정점 개수, 간선 개수, 시작노드
n,m,v = map(int, input().split())

visited_1 = [False] * (n + 1) # 방문할 리스트
visited_2 = [False] * (n + 1) # 방문할 리스트
# graph = 그래프를 인접 리스트 형태로 초기화
# n+1 -> 0을 비우고 1부터 시작하기 위함.
graph = [[] for _ in range(n+1)]

# 간선은 양방향 - 정점 번호 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# dfs
def dfs(graph,start,visited_1):
    visited_1[start] = True # 현재 노드 방문했다고 표시
    print(start, end=' ')  # 방문한 노드 출력

    for neighbor in graph[start]: # 현재 노드와 연결된 이웃 노드 탐색 
        if not visited_1[neighbor]: # 이웃 노드 방문x
            dfs(graph,neighbor,visited_1) # 해당 노드로 재귀 호출

# bfs
def bfs(graph, start, visited_2):
    queue = deque([start])
    visited_2[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')  # 방문한 노드 출력
        for neighbor in graph[node]:  # 현재 노드와 연결된 노드 탐색
            if not visited_2[neighbor]:
                queue.append(neighbor)
                visited_2[neighbor] = True


dfs(graph, v, visited_1)
print()
bfs(graph, v, visited_2)