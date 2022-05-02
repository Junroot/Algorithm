board_size, shark_count, smell_time = map(int, input().split())
board = [list(map(lambda x: [x] if x != 0 else [], map(int, input().split()))) for _ in range(board_size)]
smells = [[(0, -987654) for _ in range(board_size)] for _ in range(board_size)]
shark_directions = [0] + list(map(int, input().split()))
directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
shark_direction_priority = [[]]
left_shark = shark_count

for _ in range(shark_count):
    temp_directions = [[]]
    for _ in range(4):
        temp_directions.append(list(map(int, input().split())))
    shark_direction_priority.append(temp_directions)


def make_smells(time):
    for y in range(board_size):
        for x in range(board_size):
            for shark in board[y][x]:
                smells[y][x] = (shark, time)


def is_valid_position(y, x):
    return 0 <= x < board_size and 0 <= y < board_size


def move_sharks(time):
    global board
    new_board = [[[] for _ in range(board_size)] for _ in range(board_size)]
    for y in range(board_size):
        for x in range(board_size):
            for shark in board[y][x]:
                shark_direction = shark_directions[shark]
                is_moved = False
                for next_direction in shark_direction_priority[shark][shark_direction]:
                    direction = directions[next_direction]
                    next_y = y + direction[0]
                    next_x = x + direction[1]
                    if is_valid_position(next_y, next_x) and time - smells[next_y][next_x][1] >= smell_time:
                        new_board[next_y][next_x].append(shark)
                        shark_directions[shark] = next_direction
                        is_moved = True
                        break
                if not is_moved:
                    for next_direction in shark_direction_priority[shark][shark_direction]:
                        direction = directions[next_direction]
                        next_y = y + direction[0]
                        next_x = x + direction[1]
                        if is_valid_position(next_y, next_x) and time - smells[next_y][next_x][1] < smell_time and \
                                smells[next_y][next_x][0] == shark:
                            new_board[next_y][next_x].append(shark)
                            shark_directions[shark] = next_direction
                            break
    board = new_board


def kill_sharks():
    global left_shark
    for y in range(board_size):
        for x in range(board_size):
            if len(board[y][x]) > 1:
                left_shark -= (len(board[y][x])) - 1
                strongest_shark = min(board[y][x])
                board[y][x] = [strongest_shark]


for time in range(1000):
    make_smells(time)
    move_sharks(time)
    kill_sharks()
    if left_shark == 1:
        print(time + 1)
        exit()

print(-1)
