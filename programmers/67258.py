def solution(gems):
    gem_counts = dict()
    needed_gems = set(gems)
    for gem in list(set(gems)):
        gem_counts[gem] = 0

    gem_counts[gems[0]] = 1
    needed_gems -= {gems[0]}
    result = [1, len(gems)]
    end = 0

    for start in range(len(gems) - len(gem_counts) + 1):
        while len(needed_gems) != 0 and end < len(gems) - 1:
            end += 1
            gem_counts[gems[end]] += 1
            needed_gems -= {gems[end]}

        if len(needed_gems) == 0 and result[1] - result[0] > end - start:
            result = [start + 1, end + 1]

        gem_counts[gems[start]] -= 1
        if gem_counts[gems[start]] == 0:
            needed_gems.add(gems[start])
    return result
