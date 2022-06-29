from itertools import combinations


def is_valid(combination, relation):
    keys = set(map(lambda row: tuple([row[i] for i in combination]), relation))
    return len(keys) == len(relation)


def is_minimal(candidate_keys, key):
    for candidate_key in candidate_keys:
        if candidate_key.issubset(key):
            return False
    return True


def solution(relation):
    columns = set([i for i in range(len(relation[0]))])
    candidate_keys = []
    for key_size in range(1, len(columns) + 1):
        for combination in combinations(columns, key_size):
            combination = set(combination)
            if is_valid(combination, relation) and is_minimal(candidate_keys, combination):
                candidate_keys.append(combination)

    return len(candidate_keys)
