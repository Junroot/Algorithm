def get_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def solution(numbers, hand):
    answer = ""
    positions = [(1, 3)]
    for y in range(3):
        for x in range(3):
            positions.append((x, y))

    is_right_hand = (hand[0] == "r")
    left_position = (0, 3)
    right_position = (2, 3)

    for number in numbers:
        x, y = positions[number]
        if x == 0:
            left_position = (x, y)
            answer += "L"
        elif x == 2:
            right_position = (x, y)
            answer += "R"
        else:
            left_distance = get_distance(left_position[0], left_position[1], x, y)
            right_distance = get_distance(right_position[0], right_position[1], x, y)
            if left_distance < right_distance:
                left_position = (x, y)
                answer += "L"
            elif right_distance < left_distance:
                right_position = (x, y)
                answer += "R"
            else:
                if is_right_hand:
                    right_position = (x, y)
                    answer += "R"
                else:
                    left_position = (x, y)
                    answer += "L"
    return answer


