money = 1000 - int(input())

def calc(coin):
    global money
    tmp = money // coin
    money %= coin
    return tmp

result = 0
for coin in [500, 100, 50, 10, 5, 1]:
    result += calc(coin)

print(result)