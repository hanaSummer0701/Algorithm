n = int(input())
for i in range(n):
    num = i+sum(map(int, str(i)))
    if num==n:
        print(i)
        break
else:
    print(0)