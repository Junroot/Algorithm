def get_positions_to_delete(m, n, board):
    result = set()
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == '-':
                continue
            if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                result = result.union({(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)})
    return result


def compress(m, n, board):
    for x in range(n):
        for y in range(m - 1, -1, -1):
            if board[y][x] == '-':
                continue
            next_y = y
            while next_y < m - 1 and board[next_y + 1][x] == '-':
                next_y += 1
            if next_y == y:
                continue
            board[next_y][x] = board[y][x]
            board[y][x] = '-'


def solution(m, n, board):
    board = list(map(list, board))
    result = 0
    while True:
        positions_to_delete = get_positions_to_delete(m, n, board)
        if len(positions_to_delete) == 0:
            break
        result += len(positions_to_delete)
        for position in positions_to_delete:
            board[position[0]][position[1]] = '-'
        compress(m, n, board)
    return result

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
