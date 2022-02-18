n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

cache = [0 for _ in range(k + 1)]

for weight, value in items:
    for i in range(k, weight - 1, -1):
        cache[i] = max(cache[i], cache[i - weight] + value)

print(cache[k])
