def check_to_create(x, y, a, board):
    n = len(board)
    if a == 0:
        if y == 0:
            return True
        if y > 0 and board[x][y - 1][0]:
            return True
        if (x > 0 and board[x - 1][y][1]) or (x < n and board[x][y][1]):
            return True
    elif a == 1:
        if y > 0 and (board[x][y - 1][0] or board[x + 1][y - 1][0]):
            return True
        if 0 < x < n - 1 and board[x - 1][y][1] and board[x + 1][y][1]:
            return True
    return False


def print_board(board):
    for i in range(len(board)):
        print(board[i])
    print()


def check_to_delete(x, y, a, board):
    n = len(board)
    if a == 0:
        if y < n - 1 and board[x][y + 1][0] and not check_to_create(x, y + 1, 0, board):
            return False
        if y < n and board[x][y + 1][1] and not check_to_create(x, y + 1, 1, board):
            return False
        if x > 0 and y < n and board[x - 1][y + 1][1] and not check_to_create(x - 1, y + 1, 1, board):
            return False
    elif a == 1:
        if board[x][y][0] and not check_to_create(x, y, 0, board):
            return False
        if x < n and board[x + 1][y][0] and not check_to_create(x + 1, y, 0, board):
            return False
        if x > 0 and board[x - 1][y][1] and not check_to_create(x - 1, y, 1, board):
            return False
        if x < n - 1 and board[x + 1][y][1] and not check_to_create(x + 1, y, 1, board):
            return False
    return True


def solution(n, build_frame):
    board = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]
    for operation in build_frame:
        x, y, a, b = operation[0], operation[1], operation[2], operation[3]

        if b == 1:
            if check_to_create(x, y, a, board):
                board[x][y][a] = True
        else:
            board[x][y][a] = False
            if not check_to_delete(x, y, a, board):
                board[x][y][a] = True

    result = []
    for x in range(n + 1):
        for y in range(n + 1):
            for i in range(2):
                if board[x][y][i]:
                    result.append([x, y, i])
    return result
