coins = [500, 100, 50, 10, 5, 1]

price = 1000 - int(input())
count = 0

for coin in coins:
    count += price // coin
    price = price % coin
    if price == 0:
        break

print(count)