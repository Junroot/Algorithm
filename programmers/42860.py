def solution(name):
    answer = horizontal_movement(name)
    answer += vertical_movement(name)
    return answer


def horizontal_movement(name):
    a_ranges = find_all_a_ranges(name)
    return find_min_horizontal_movement(a_ranges, len(name))


def find_all_a_ranges(name):
    result = []
    start = None
    for i in range(1, len(name)):
        if start is None and name[i] == "A":
            start = i
        elif start is not None and name[i] != "A":
            result.append((start, i - 1))
            start = None
    if start is not None:
        result.append((start, len(name) - 1))
    return result


def find_min_horizontal_movement(a_ranges, name_count):
    movements = []
    for a_range in a_ranges:
        start, end = a_range
        movements.append((start - 1) * 2 + (name_count - end - 1))
    movements.append(name_count - 1)
    return min(movements)


def vertical_movement(name):
    result = 0
    for character in name:
        result += vertical_movement_per_character(character)
    return result


def vertical_movement_per_character(character):
    result = ord(character) - ord('A')
    if result > 13:
        return 26 - result
    return result
