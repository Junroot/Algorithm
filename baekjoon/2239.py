board = [list(map(int, list(input()))) for _ in range(9)]


def next_point(x, y):
    if x == 8:
        return 0, y + 1
    return x + 1, y


def get_possible_numbers(x, y):
    duplicated_numbers = set()
    for i in range(9):
        if board[y][i] != 0:
            duplicated_numbers.add(board[y][i])
        if board[i][x] != 0:
            duplicated_numbers.add(board[i][x])

    x_group = x // 3
    y_group = y // 3

    for i in range(3):
        for j in range(3):
            if board[y_group * 3 + i][x_group * 3 + j] != 0:
                duplicated_numbers.add(board[y_group * 3 + i][x_group * 3 + j])

    return set(range(1, 10)) - duplicated_numbers


def fill(x, y):
    if y > 8:
        return True
    if board[y][x] != 0:
        return fill(*next_point(x, y))
    possible_numbers = get_possible_numbers(x, y)

    for number in possible_numbers:
        board[y][x] = number
        if fill(*next_point(x, y)):
            return True

    board[y][x] = 0
    return False


fill(0, 0)

print("\n".join(map(lambda row: "".join(map(str, row)), board)))
