def time_string_to_int(time_string):
    hour, minute = map(int, time_string.split(':'))
    return hour * 60 + minute


def time_int_to_string(time_int):
    hour = str(time_int // 60)
    minute = str(time_int % 60)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    return f'{hour}:{minute}'


def solution(n, t, m, timetable):
    timetable_ints = sorted(map(time_string_to_int, timetable))
    next_crew_index = 0
    passengers = []
    for current_time in range(9 * 60, 9 * 60 + (n - 1) * t + 1, t):
        passengers_in_bus = []
        while len(passengers_in_bus) < m and next_crew_index < len(timetable_ints) and timetable_ints[
            next_crew_index] <= current_time:
            passengers_in_bus.append(timetable_ints[next_crew_index])
            next_crew_index += 1
        passengers.append(passengers_in_bus)
    if len(passengers[-1]) == m:
        return time_int_to_string(passengers[-1][-1] - 1)
    return time_int_to_string(9 * 60 + (n - 1) * t)


print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
