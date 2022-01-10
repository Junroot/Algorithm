n = int(input())
cache = [0] * (n + 1)

cache[1] = 1
cache[2] = 3

for i in range(3, n + 1):
    cache[i] = (cache[i - 1] + cache[i - 2] * 2) % 796796

print(cache[n])

