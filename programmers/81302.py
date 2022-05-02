from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_valid_position(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def is_safe_position(x, y, place):
    queue = deque([(x, y)])
    visited = {(x, y)}
    distance = 0
    while queue:
        queue_length = len(queue)
        distance += 1
        for _ in range(queue_length):
            now_x, now_y = queue.popleft()
            for direction in directions:
                next_x = now_x + direction[0]
                next_y = now_y + direction[1]
                if is_valid_position(next_x, next_y) and (next_x, next_y) not in visited:
                    if place[next_y][next_x] == "P":
                        return False
                    elif place[next_y][next_x] == "O":
                        queue.append((next_x, next_y))
                        visited.add((next_x, next_y))
                    elif place[next_y][next_x] == "X":
                        visited.add((next_x, next_y))
        if distance >= 2:
            break
    return True


def check_place(place):
    for y in range(len(place)):
        for x in range(len(place[0])):
            if place[y][x] == "P" and not is_safe_position(x, y, place):
                return False
    return True



def solution(places):
    answer = []

    for place in places:
        if check_place(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer