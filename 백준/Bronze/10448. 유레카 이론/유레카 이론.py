# 10448
triangle = [n*(n+1)//2 for n in range(1,46) if n*(n+1)//2 <=1001]

def trianglesum(k):
    for i in triangle:
        for j in triangle:
            for h in triangle:
                if i+j+h == k:
                    return 1
    return 0

num = int(input())
for _ in range(num):
    k = int(input())
    print(trianglesum(k))
