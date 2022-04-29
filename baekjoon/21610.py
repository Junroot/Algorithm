board_length, movement_count = map(int, input().split())
buckets = [[0 for _ in range(board_length + 1)]] \
          + [[0] + list(map(int, input().split())) for _ in range(board_length)]
directions = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
movements = [tuple(map(int, input(). split())) for _ in range(movement_count)]
clouds = {(1, board_length), (2, board_length), (1, board_length - 1), (2, board_length - 1)}


def get_movement(direction, distance):
    x = directions[direction][0]
    y = directions[direction][1]
    x = x * (distance % board_length)
    y = y * (distance % board_length)
    return x, y


def drop_rain():
    for cloud in clouds:
        buckets[cloud[1]][cloud[0]] += 1


def get_diagonals(x, y):
    relative_positions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    results = []
    for relative_position in relative_positions:
        new_x = x + relative_position[0]
        new_y = y + relative_position[1]
        if 0 < new_x <= board_length and 0 < new_y <= board_length:
            results.append((new_x, new_y))
    return results


def copy_water():
    for x, y in clouds:
        diagonals = get_diagonals(x, y)
        for diagonal in diagonals:
            if buckets[diagonal[1]][diagonal[0]] > 0:
                buckets[y][x] += 1


def update_clouds():
    global clouds
    new_clouds = set()
    for y in range(1, board_length + 1):
        for x in range(1, board_length + 1):
            if buckets[y][x] >= 2 and (x, y) not in clouds:
                buckets[y][x] -= 2
                new_clouds.add((x, y))
    clouds = new_clouds


def move_clouds(x_movement, y_movement):
    global clouds
    new_clouds = set()
    for x, y in clouds:
        new_x = (x + x_movement + board_length - 1) % board_length + 1
        new_y = (y + y_movement + board_length - 1) % board_length + 1
        new_clouds.add((new_x, new_y))

    clouds = new_clouds


for direction, distance in movements:
    x_movement, y_movement = get_movement(direction, distance)
    move_clouds(x_movement, y_movement)
    drop_rain()
    copy_water()
    update_clouds()

print(sum(map(sum, buckets)))
