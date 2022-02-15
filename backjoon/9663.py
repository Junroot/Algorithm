n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]


def add_queen(row_index, column_index, number):
    for i in range(n):
        board[row_index][i] += number
        board[i][column_index] += number

    for x in range(max(0, column_index - row_index), min(n, (n - row_index) + column_index)):
        board[row_index + x - column_index][x] += number

    for x in range(max(0, row_index + column_index - (n - 1)), min(n, row_index + column_index + 1)):
        board[row_index + column_index - x][x] += number

    board[row_index][column_index] -= 3 * number


def count_queen_putting(row_index):
    result = 0
    if row_index == n - 1:
        return sum(map(lambda point: point == 0, board[row_index]))
    for column_index in range(n):
        if board[row_index][column_index] == 0:
            add_queen(row_index, column_index, 1)
            result += count_queen_putting(row_index + 1)
            add_queen(row_index, column_index, -1)
    return result


print(count_queen_putting(0))
