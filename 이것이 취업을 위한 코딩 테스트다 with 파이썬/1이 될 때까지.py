n, k = map(int, input().split())

count = 0

while n != 1:
    remainder = n % k
    if remainder == 0:
        n = n // k
        count += 1
    else:
        count += remainder
        n -= remainder

print(count)