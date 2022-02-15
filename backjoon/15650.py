n, m = map(int, input().split())


def get_sequences(min_number, left):
    if left == 0:
        return [[]]
    if n - min_number == left - 1:
        return [list(map(str, range(min_number, n + 1)))]
    r = []
    for sub in get_sequences(min_number + 1, left - 1):
        r.append([str(min_number)] + sub)
    r.extend(get_sequences(min_number + 1, left))
    return r


for result in get_sequences(1, m):
    print(" ".join(result))