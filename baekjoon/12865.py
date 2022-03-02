n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
items.sort()
cache = []


def highest_value(index, left_weight):
    if index >= n:
        return 0
    weight, value = items[index][0], items[index][1]
    if left_weight < weight:
        return 0
    if (index, left_weight) in cache:
        return cache[(index, left_weight)]
    cache[(index, left_weight)] = max(highest_value(index + 1, left_weight), value + highest_value(index + 1, left_weight - weight))
    return cache[(index, left_weight)]


print(highest_value(0, k))
