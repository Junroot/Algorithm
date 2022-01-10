n, m = map(int, input().split())
currencies = []
for _ in range(n):
    currencies.append(int(input()))
min_currency = min(currencies)

cache = [10001] * (m + 1)

for currency in currencies:
    if currency <= m:
        cache[currency] = 1

for i in range(min_currency + 1, m + 1):
    for currency in currencies:
        if i - currency > 0:
            cache[i] = min(min(cache[i - currency] + 1, 10001), cache[i])

if cache[m] > 10000:
    print(-1)
else:
    print(cache[m])
