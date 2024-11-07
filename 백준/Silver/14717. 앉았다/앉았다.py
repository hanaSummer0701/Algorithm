from itertools import combinations

a, b = map(int, input().split())

# 모든 카드 설정
card = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
my_card = [a, b]
card_list = card[:]

# 중복 계산을 위해 남은 카드 계산
for num in my_card:
    card_list.remove(num)
card_combinations = list(combinations(card_list, 2))

# 족보 판별 함수
def get_card(x, y):
    if x == y:
        return '땡', x
    else:
        return '끗', (x + y) % 10

# 영학이의 패
my_card_type, my_card_value = get_card(a, b)

# 승리 조건 계산
win_count = 0
for c in card_combinations:
    opp_card_type, opp_card_value = get_card(c[0], c[1])
    
    # 영학이의 승리 조건
    if (my_card_type == '땡' and opp_card_type == '끗') or \
       (my_card_type == opp_card_type and my_card_value > opp_card_value):
        # 중복 조합 개수를 반영하여 더하기
        if c[0] == c[1]:  
            win_count += 1  # 같은 카드일 경우
        else:
            win_count += 1  # 서로 다른 카드일 경우 두 가지 경우
          
total_combinations = len(card_combinations)
win_prob = win_count / total_combinations
print(f"{win_prob:.3f}")
