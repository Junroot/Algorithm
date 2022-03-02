n = int(input())
numbers = list(map(int, input().split()))
max_number = max(numbers)

primes = set([i for i in range(2, max_number + 1)])

for i in range(2, int(max_number ** 0.5) + 1):
    primes -= set(range(i * 2, max_number + 1, i))

count = 0
for number in numbers:
    if number in primes:
        count += 1

print(count)
