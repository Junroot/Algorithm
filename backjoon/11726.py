cache = [0, 1, 2]

n = int(input())

for i in range(3, n + 1):
    cache.append((cache[i - 1] + cache[i - 2]) % 10007)

print(cache[n])
