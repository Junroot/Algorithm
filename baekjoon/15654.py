n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
used = [False for _ in range(n)]


def all_sequences(length):
    if length == 0:
        return [[]]
    result = []
    for i in range(n):
        if used[i]:
            continue
        used[i] = True
        sub_sequences = all_sequences(length - 1)
        for sub_sequence in sub_sequences:
            result.append([numbers[i]] + sub_sequence)
        used[i] = False
    return result


for sequence in all_sequences(m):
    print(" ".join(map(str, sequence)))
