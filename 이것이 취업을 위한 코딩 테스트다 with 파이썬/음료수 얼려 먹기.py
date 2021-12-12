from collections import deque


def is_possible_point(point, board):
    return 0 <= point[1] < len(board) and 0 <= point[0] < len(board[0])


def bfs(board, x, y):
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = deque([(x, y)])
    while queue:
        current_point = queue.popleft()
        board[current_point[1]][current_point[0]] = "1"
        for direction in directions:
            next_point = (current_point[0] + direction[0], current_point[1] + direction[1])
            if is_possible_point(next_point, board) and board[next_point[1]][next_point[0]] == "0":
                queue.append(next_point)


n, m = map(int, input().split())
result = 0
board = []

for i in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        if board[i][j] == "0":
            result += 1
            bfs(board, j, i)

print(result)
