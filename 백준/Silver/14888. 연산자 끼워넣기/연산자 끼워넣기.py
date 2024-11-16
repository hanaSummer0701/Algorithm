# 14888
from itertools import permutations
n=int(input())
n_list = list(map(int, input().split()))
oper = list(map(int, input().split()))

# 연산자를 리스트로 - 연산자를 각 개수만큼 생성하여 리스트에 담음
operators = (
    ["+"] * oper[0]
    + ["-"] * oper[1]
    + ["*"] * oper[2]
    + ["/"] * oper[3]
)
# 순서 고려해서 연산자 리스트 형성+중복제거
oper_permutation = set(permutations(operators, n-1))

# 최댓값과 최솟값 초기화
max_result = -float("inf")
min_result = float("inf")


for oper_set in oper_permutation:
    result = n_list[0]
    for i in range(n-1):
        if oper_set[i] == '+':
            result += n_list[i+1]
        elif oper_set[i] == '-':
            result -= n_list[i+1]
        elif oper_set[i] == '*':
            result *= n_list[i+1]
        elif oper_set[i] == '/':
            if result<0:
                result = -(-result//n_list[i+1])
            else:
                result //= n_list[i+1]

    # 최댓값과 최솟값 갱신
    max_result = max(max_result, result)
    min_result = min(min_result, result)
print(max_result, min_result)