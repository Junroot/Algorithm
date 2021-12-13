def solution(citations):
    citations.sort(reverse=True)
    index = 0
    for h in range(len(citations), -1, -1):
        while index < len(citations) and h <= citations[index]:
            index += 1
        if index >= h:
            return h
        if index >= len(citations):
            break

    return 0


print(solution([1]))
