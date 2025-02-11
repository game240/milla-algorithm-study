def buy_all(i, balance, stock):
    global stock_price
    
    while balance >= stock_price[i]:
        balance -= stock_price[i]
        stock += 1

    return balance, stock

def sell_all(i, balance, stock):
    balance += stock * stock_price[i]
    stock = 0

    return balance, stock

balance_BNP = int(input())
balance_TIMING = balance_BNP

stock_price = list(map(int, input().split()))

stock_BNP = 0
for i in range(len(stock_price)):
    balance_BNP, stock_BNP = buy_all(i, balance_BNP, stock_BNP)

stock_TIMING = 0
increased_by_previous = 0
decreased_by_previous = 0
for i in range(len(stock_price)):
    if i == 0:
        continue
    
    # 전일 대비 상승치 계산
    if stock_price[i] > stock_price[i - 1]:
        increased_by_previous += 1
    else:
        increased_by_previous = 0
    if stock_price[i] < stock_price[i - 1]:
        decreased_by_previous += 1
    else:
        decreased_by_previous = 0

    if increased_by_previous >= 3:
        balance_TIMING, stock_TIMING = sell_all(i, balance_TIMING, stock_TIMING)
    if decreased_by_previous >= 3:
        balance_TIMING, stock_TIMING = buy_all(i, balance_TIMING, stock_TIMING)

# (현금 + 1월 14일의 주가 × 주식 수)
total_BNP = balance_BNP + stock_price[len(stock_price) - 1] * stock_BNP
total_TIMING = balance_TIMING + stock_price[len(stock_price) - 1] * stock_TIMING

if total_BNP > total_TIMING:
    print('BNP')
elif total_BNP < total_TIMING:
    print('TIMING')
else:
    print('SAMESAME')
