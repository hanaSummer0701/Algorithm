# 1330
a, b = map(int, input().split())

def jud (x, y):
    if x > y:
        print('>')
    elif x < y:
        print('<')
    else:
        print('==')
jud(a, b)