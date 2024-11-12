# 20546
money = int(input()) # 초기 돈
machineduck = list(map(int, input().split())) # 주가 리스트

def bnp(money, prices):
    stock=0
    for price in prices:
        if money >= price:
            stock += money//price
            money = money%price
    return money, stock # 남은 돈, 주식

def time(money, prices):
    stocks = 0
    for i in range(3, len(prices)):
        # 3일 연속 하락하면 매수
        if prices[i-3] > prices[i-2] > prices[i-1] > prices[i]:
            if money >= prices[i]:
                stocks += money // prices[i]
                money %= prices[i]
        # 3일 연속 상승하면 매도
        elif prices[i-3] < prices[i-2] < prices[i-1] < prices[i]:
            money += stocks * prices[i]
            stocks = 0
    return money, stocks

j_money, j_stock = bnp(money, machineduck)
s_money, s_stock = time(money, machineduck)

final_j = j_money+j_stock * machineduck[-1]
final_s = s_money+s_stock * machineduck[-1]

# 결과 출력
if final_j > final_s:
    print("BNP")
elif final_j < final_s:
    print("TIMING")
else:
    print("SAMESAME")