def get_line(board, x1, y1, x2, y2):
    if y1 == y2:
        return board[y1][x1:x2 + 1]
    line = []
    for i in range(y1, y2 + 1):
        line.append(board[i][x1])
    return line


def find_min_number(borders):
    min_number = 1000000
    for border in borders:
        min_number = min(min_number, min(border))
    return min_number


def solution(rows, columns, queries):
    answer = []
    board = []

    for row in range(rows):
        entry = []
        for column in range(columns):
            entry.append(columns * row + column + 1)
        board.append(entry)

    for query in queries:
        y1, x1, y2, x2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        borders = [get_line(board, x1, y1, x2 - 1, y1), get_line(board, x2, y1, x2, y2 - 1),
                   get_line(board, x1 + 1, y2, x2, y2), get_line(board, x1, y1 + 1, x1, y2)]
        answer.append(find_min_number(borders))

        for i in range(len(borders[0])):
            board[y1][x1 + 1 + i] = borders[0][i]
            board[y2][x1 + i] = borders[2][i]

        for i in range(len(borders[1])):
            board[y1 + 1 + i][x2] = borders[1][i]
            board[y1 + i][x1] = borders[3][i]

    return answer

