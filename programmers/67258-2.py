from collections import defaultdict


def solution(gems):
    result = [1, len(gems)]
    gem_type_count = 1
    gem_types = set(gems)
    total_gem_type = len(gem_types)
    gem_count = defaultdict(int)
    gem_count[gems[0]] = 1

    end_index = 0
    for start_index in range(len(gems)):
        while gem_type_count < total_gem_type:
            end_index += 1
            if end_index == len(gems):
                return result
            gem_count[gems[end_index]] += 1
            if gem_count[gems[end_index]] == 1:
                gem_type_count += 1

        if end_index - start_index < result[1] - result[0]:
            result = [start_index + 1, end_index + 1]

        gem_count[gems[start_index]] -= 1
        if gem_count[gems[start_index]] == 0:
            gem_type_count -= 1

    return result

