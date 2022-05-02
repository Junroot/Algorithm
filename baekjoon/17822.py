from collections import deque

circle_count, numbers_in_circle_count, rotation_count = map(int, input().split())
circles = [deque(list(map(int, input().split()))) for _ in range(circle_count)]
rotations = [tuple(map(int, input().split())) for _ in range(rotation_count)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def rotate(x, direction, rotation_distance):
    for i in range(x - 1, circle_count, x):
        if direction == 0:
            for _ in range(rotation_distance):
                number = circles[i].pop()
                circles[i].appendleft(number)
        else:
            for _ in range(rotation_distance):
                number = circles[i].popleft()
                circles[i].append(number)


def remove_adjacent_numbers():
    is_removed = False
    for i in range(circle_count):
        for j in range(numbers_in_circle_count):
            if circles[i][j] != 0:
                visited = {(i, j)}
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.pop()
                    for direction in directions:
                        new_y = y + direction[0]
                        new_x = (x + direction[1] + numbers_in_circle_count) % numbers_in_circle_count
                        if 0 <= new_y < circle_count and (new_y, new_x) not in visited and circles[new_y][new_x] == circles[i][j]:
                            visited.add((new_y, new_x))
                            queue.appendleft((new_y, new_x))
                if len(visited) > 1:
                    for y, x in visited:
                        circles[y][x] = 0
                        is_removed = True
    return is_removed


def update_numbers():
    total_numbers = 0
    number_count = 0
    for i in range(circle_count):
        for j in range(numbers_in_circle_count):
            if circles[i][j] != 0:
                total_numbers += circles[i][j]
                number_count += 1
    for i in range(circle_count):
        for j in range(numbers_in_circle_count):
            if circles[i][j] != 0:
                if circles[i][j] * number_count > total_numbers:
                    circles[i][j] -= 1
                elif circles[i][j] * number_count < total_numbers:
                    circles[i][j] += 1


for x, direction, rotation_distance in rotations:
    rotate(x, direction, rotation_distance)
    is_removed = remove_adjacent_numbers()
    if not is_removed:
        update_numbers()

total = 0

for i in range(circle_count):
    for j in range(numbers_in_circle_count):
        if circles[i][j] != 0:
            total += circles[i][j]

print(total)
