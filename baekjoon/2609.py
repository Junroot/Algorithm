import sys

a, b = map(int, sys.stdin.readline().split())


def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        return gcd(b, a)
    return gcd(b, a % b)


result = gcd(a, b)
print(result)
print(a * b // result)