x = int(input())
cache = [0] * 30001
divisors = [2, 3, 5]

for num in range(2, x + 1):
    cache[num] = cache[num - 1] + 1
    for divisor in divisors:
        if num % divisor == 0:
            cache[num] = min(cache[num // divisor] + 1, cache[num])

print(cache[x])
