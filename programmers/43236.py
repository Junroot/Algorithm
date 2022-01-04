def solution(distance, rocks, n):
    rocks.sort()
    rocks.insert(0, 0)
    rocks.append(distance)

    start = 0
    end = distance

    result = -1
    while end >= start:
        expected = (start + end) // 2

        count = 0
        latest = 0
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[latest] >= expected:
                latest = i
            else:
                count += 1

        if count > n:
            end = expected - 1
        else:
            result = expected
            start = expected + 1
    return result
