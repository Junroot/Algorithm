shapes = [
    [[1, 1, 1, 1]],
    [[1, 1],
     [1, 1]],
    [[1, 0],
     [1, 0],
     [1, 1]],
    [[1, 0],
     [1, 1],
     [0, 1]],
    [[1, 1, 1],
     [0, 1, 0]]
]

height, width = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]

result = 0

for shape in shapes:
    for _ in range(4):
        for i in range(height - len(shape) + 1):
            for j in range(width - len(shape[0]) + 1):
                total = 0
                for y in range(len(shape)):
                    for x in range(len(shape[0])):
                        total += board[i + y][j + x] * shape[y][x]
                result = max(total, result)

                total = 0
                for y in range(len(shape)):
                    for x in range(len(shape[0])):
                        total += board[i + y][j + x] * shape[y][len(shape[0]) - 1 - x]
                result = max(total, result)

                total = 0
                for y in range(len(shape)):
                    for x in range(len(shape[0])):
                        total += board[i + y][j + x] * shape[len(shape) - 1 - y][x]
                result = max(total, result)

        new_shape = [[0 for _ in range(len(shape))] for _ in range(len(shape[0]))]
        for i in range(len(shape[0])):
            for j in range(len(shape)):
                new_shape[i][j] = shape[j][len(shape[0]) - i - 1]
        shape = new_shape

print(result)