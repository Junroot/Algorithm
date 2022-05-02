board_size, fire_ball_count, movement_count = map(int, input().split())
board = [[[] for _ in range(board_size + 1)] for _ in range(board_size + 1)]
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(fire_ball_count):
    row, column, measure, speed, direction = map(int, input().split())
    board[row][column].append((measure, speed, direction))


def move_fire_balls():
    global board
    new_board = [[[] for _ in range(board_size + 1)] for _ in range(board_size + 1)]
    for row in range(1, board_size + 1):
        for column in range(1, board_size + 1):
            for measure, speed, direction_index in board[row][column]:
                direction = directions[direction_index]
                new_row = (row + direction[0] * (speed % board_size) + board_size - 1) % board_size + 1
                new_column = (column + direction[1] * (speed % board_size) + board_size - 1) % board_size + 1
                new_board[new_row][new_column].append((measure, speed, direction_index))
    board = new_board


def update_fire_balls():
    for row in range(1, board_size + 1):
        for column in range(1, board_size + 1):
            if len(board[row][column]) < 2:
                continue
            total_measure = 0
            total_speed = 0
            is_first_direction_odd = (board[row][column][0][2] % 2) == 1
            is_all_ood_or_even = True
            for measure, speed, direction_index in board[row][column]:
                total_measure += measure
                total_speed += speed
                if is_first_direction_odd and direction_index % 2 == 0:
                    is_all_ood_or_even = False
                if not is_first_direction_odd and direction_index % 2 == 1:
                    is_all_ood_or_even = False
            new_measure = total_measure // 5
            new_speed = total_speed // len(board[row][column])
            board[row][column] = []
            if new_measure != 0:
                if is_all_ood_or_even:
                    for direction in [0, 2, 4, 6]:
                        board[row][column].append((new_measure, new_speed, direction))
                else:
                    for direction in [1, 3, 5, 7]:
                        board[row][column].append((new_measure, new_speed, direction))


for _ in range(movement_count):
    move_fire_balls()
    update_fire_balls()

total_measure = 0

for row in range(1, board_size + 1):
    for column in range(1, board_size + 1):
        for measure, speed, direction_index in board[row][column]:
            total_measure += measure

print(total_measure)
