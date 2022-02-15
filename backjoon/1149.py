from sys import stdin

MAX_INT = 987654321
n = int(stdin.readline())
costs = [list(map(int, stdin.readline().split())) for _ in range(n)]
cache = [[-1 for _ in range(3)] for _ in range(n)]


def min_cost(index, last_color):
    if index >= n:
        return 0
    if last_color != -1 and cache[index][last_color] != -1:
        return cache[index][last_color]
    result = MAX_INT
    for color in range(3):
        if color == last_color:
            continue
        result = min(result, costs[index][color] + min_cost(index + 1, color))
    if last_color != -1:
        cache[index][last_color] = result
    return result


print(min_cost(0, -1))
