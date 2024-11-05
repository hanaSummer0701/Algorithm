from itertools import combinations
item=[int(input()) for _ in range(9)]
for num_list in combinations(item, 7):
    if sum(num_list) == 100:
        for a in sorted(num_list):
            print(a)
        break
