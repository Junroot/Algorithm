fish_count, spell_count = map(int, input().split())
directions = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
board = [[[0 for _ in range(9)] for _ in range(5)] for _ in range(5)]
new_board = [[[0 for _ in range(9)] for _ in range(5)] for _ in range(5)]
smells = [[-90 for _ in range(5)] for _ in range(5)]
for _ in range(fish_count):
    x, y, direction = map(int, input().split())
    board[x][y][direction] += 1
    new_board[x][y][direction] += 1
shark = tuple(map(int, input().split()))
shark_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def is_valid_position(x, y):
    return 1 <= x <= 4 and 1 <= y <= 4

def get_total_fishes(x, y):
    return sum(new_board[x][y])

def move_fishes(turn):
    global new_board
    moved_board = [[[0 for _ in range(9)] for _ in range(5)] for _ in range(5)]
    for x in range(1, 5):
        for y in range(1, 5):
            for _ in range(8):
                for d in range(1, 9):
                    direction = directions[d]
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    if is_valid_position(new_x, new_y) and (new_x, new_y) != shark and turn - smells[new_x][new_y] > 2:
                        moved_board[new_x][new_y][d] += new_board[x][y][d]
                        new_board[x][y][d] = 0
                new_fishes = [0]
                for i in range(1, 9):
                    new_fishes.append(new_board[x][y][i % 8 + 1])
                new_board[x][y] = new_fishes
            for d in range(1, 9):
                moved_board[x][y][d] += new_board[x][y][d]
    new_board = moved_board


def get_shark_path(x, y, length):
    if length == 0:
        return 0, []
    path = []
    eaten_fishes = -1
    for direction in shark_directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if is_valid_position(new_x, new_y):
            new_position_fishes = get_total_fishes(new_x, new_y)
            temp = new_board[new_x][new_y]
            new_board[new_x][new_y] = [0 for _ in range(9)]
            sub_fishes, sub_path = get_shark_path(new_x, new_y, length - 1)
            new_board[new_x][new_y] = temp
            if eaten_fishes < sub_fishes + new_position_fishes:
                eaten_fishes = sub_fishes + new_position_fishes
                path = [(new_x, new_y)] + sub_path
    return eaten_fishes, path


def use_spell():
    for x in range(1, 5):
        for y in range(1, 5):
            for d in range(1, 9):
                new_board[x][y][d] += board[x][y][d]
                board[x][y][d] = new_board[x][y][d]


for turn in range(spell_count):
    move_fishes(turn)
    eaten_fishes, path = get_shark_path(shark[0], shark[1], 3)
    for x, y in path:
        if get_total_fishes(x, y) > 0:
            smells[x][y] = turn
            new_board[x][y] = [0 for _ in range(9)]
    shark = path[-1]
    use_spell()

result = 0
for x in range(1, 5):
    for y in range(1, 5):
        result += get_total_fishes(x, y)
print(result)
