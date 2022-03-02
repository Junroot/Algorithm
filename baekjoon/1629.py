a, b, c = map(int, input().split())
cache = dict()


def power(base, exponent, divisor):
    if exponent == 1:
        return base % divisor
    if exponent in cache:
        return cache[exponent]
    if exponent % 2 == 1:
        cache[exponent] = (power(base, exponent - 1, divisor) * base) % divisor
    else:
        cache[exponent] = (power(base, exponent // 2, divisor) ** 2) % divisor
    return cache[exponent]


print(power(a, b, c))
