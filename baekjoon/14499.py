board_height, board_width, y, x, command_count = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(board_height)]
directions = list(map(int, input().split()))
movements = [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]

dice = [0, 0, 0, 0, 0, 0]


def rotate_dice(direction):
    if direction == 1:
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direction == 2:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif direction == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif direction == 4:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]


def is_valid_position(x, y):
    return 0 <= x < board_width and 0 <= y < board_height


def interact_board():
    if board[y][x] == 0:
        board[y][x] = dice[5]
    else:
        dice[5] = board[y][x]
        board[y][x] = 0


for direction in directions:
    next_x = x + movements[direction][0]
    next_y = y + movements[direction][1]
    if not is_valid_position(next_x, next_y):
        continue
    x = next_x
    y = next_y
    rotate_dice(direction)
    interact_board()
    print(dice[0])

