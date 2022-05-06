def string_to_list(s):
    result = []
    current_set = None
    is_opened = False
    number = 0
    for character in s[1:-1]:
        if '0' <= character <= '9':
            number = number * 10 + int(character)
        elif character == '{':
            current_set = set()
            is_opened = True
        elif character == '}':
            current_set.add(number)
            is_opened = False
            number = 0
            result.append(current_set)
        elif character == ',' and is_opened:
            current_set.add(number)
            number = 0
    return sorted(result, key=lambda x: len(x))


def solution(s):
    answer = []
    tuple_set = [set()] + string_to_list(s)

    for i in range(1, len(tuple_set)):
        answer.append((tuple_set[i] - tuple_set[i - 1]).pop())
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
