def get_number_of_people(times, current_time):
    result = 0
    left = times[0]
    for time in times:
        result += current_time // time
        left = min(left, current_time % time)
    return result, left


def solution(n, times):
    start, end = 0, max(times) * n

    result = -1
    while end >= start:
        time = (start + end) // 2
        number_of_people, min_left = get_number_of_people(times, time)
        if number_of_people >= n:
            result = time
            end = time - 1
        else:
            start = time + 1

    return result


print(solution(10, [6, 8, 10]))
