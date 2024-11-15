# 14889

from itertools import combinations

n=int(input())
# 능력치 2차원 배열
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

# 팀의 능력치 합 계산 함수
def team_score(team):
    score = 0
    for i in team:
        for j in team:
            score += s[i][j]
    return score

players=list(range(n)) # 모든 선수 번호 담은 리스트
min_score = float('inf') # 능력치 차이 최소값 저장 - 초기값=무한

for start_team in combinations(players, n//2):
    link_team = list(set(players)-set(start_team))
    start_score = team_score(start_team)
    link_score = team_score(link_team)
    min_score = min(min_score, abs(start_score - link_score))

print(min_score)