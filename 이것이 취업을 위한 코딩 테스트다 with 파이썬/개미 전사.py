n = int(input())
foods = list(map(int, input().split()))
cache = [0] * 101

cache[0] = foods[0]
cache[1] = max(foods[0], foods[1])
for i in range(2, n):
    cache[i] = max(foods[i] + cache[i - 2], cache[i - 1])

print(cache[n - 1])
