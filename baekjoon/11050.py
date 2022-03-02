import sys

cache = [-1 for _ in range(11)]

n, k = map(int, sys.stdin.readline().split())


def factorial(number):
    if number == 1 or number == 0:
        return 1
    if cache[number] != -1:
        return cache[number]
    cache[number] = number * factorial(number - 1)
    return cache[number]


print(int(factorial(n) / factorial(k) / factorial(n - k)))
