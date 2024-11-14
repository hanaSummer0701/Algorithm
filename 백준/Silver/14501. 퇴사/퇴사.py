#14501
n = int(input())
timetable = []
for _ in range(n):
    t, p = map(int, input().split())
    timetable.append((t,p))

# 수익을 저장할 DP 테이블 생성
money = [0] * (n + 1)

# i를 역순으로 진행하며 i~n까지 얻을 수 있는 최대 수익 계산
for i in range(n-1, -1, -1):
    time = timetable[i][0]
    pay = timetable[i][1]
    # 상담 가능 - 날짜+상담시간<=퇴사일
    if i + time <= n:
        # 상담 선택0, 선택x시 중 최댓값
        # i번째 날 상담 선택 시 수익, i번째 상담 하지 않았을 때 수익
        money[i] =  max(pay + money[i + time], money[i+1])
    else:
        # 다음날 최대 수익 가져옴
        money[i] = money[i+1]
print(money[0])