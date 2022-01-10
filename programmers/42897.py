def line_solution(money):
    if len(money) == 1:
        return money[0]
    cache = [money[0], max(money[0], money[1])]
    for i in range(2, len(money)):
        cache.append(max(money[i] + cache[i - 2], cache[i - 1]))
    return cache[len(money) - 1]


def solution(money):
    return max(money[0] + line_solution(money[2:-1]), line_solution(money[1:]))

