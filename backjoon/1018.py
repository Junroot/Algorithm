import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append(sys.stdin.readline())


def count_difference_when_first_square(x, y):
    result = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and board[y + i][x + j] != 'W':
                result += 1
            elif (i + j) % 2 == 1 and board[y + i][x + j] == 'W':
                result += 1
    return min(result, 64 - result)


result = 64
for i in range(n - 7):
    for j in range(m - 7):
        result = min(result, count_difference_when_first_square(j, i))
print(result)
