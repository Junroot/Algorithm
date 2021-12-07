n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
numbers.reverse()

secondCount = m // (k + 1)

result = numbers[1] * secondCount + numbers[0] * (m - secondCount)
print(result)