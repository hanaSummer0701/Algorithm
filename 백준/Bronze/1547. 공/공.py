# 1547
cup = [1,2,3]
m = int(input())

for i in range(m):    
        x,y = map(int, input().split())
        X = cup.index(x)
        Y = cup.index(y)
        cup[X],cup[Y] = cup[Y], cup[X]
print(cup[0])
