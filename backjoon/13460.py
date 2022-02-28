from sys import stdin
from collections import deque

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
n, m = map(int, stdin.readline().split())
board = []
queue = deque()

r_start = None
b_start = None
destination = None

for i in range(n):
    row = stdin.readline().rstrip()
    board.append(row)
    r_index = row.find("R")
    b_index = row.find("B")
    d_index = row.find("O")
    if d_index != -1:
        destination = (d_index, i)
    if r_index != -1:
        r_start = (r_index, i)
    if b_index != -1:
        b_start = (b_index, i)

queue.append((0, r_start, b_start))


def tilt(r, b, direction):
    movable = True
    while movable:
        movable = False
        next_r = (r[0] + direction[0], r[1] + direction[1])
        next_b = (b[0] + direction[0], b[1] + direction[1])
        if r != destination and board[next_r[1]][next_r[0]] != "#" and (next_r != b or b == destination):
            r = next_r
            movable = True
        if b != destination and board[next_b[1]][next_b[0]] != "#" and (next_b != r or r == destination):
            b = next_b
            movable = True
    return r, b


while queue:
    count, current_r, current_b = queue.popleft()
    if count == 10:
        continue
    for direction in directions:
        next_r, next_b = tilt(current_r, current_b, direction)
        if next_b == destination:
            continue
        if next_r == destination:
            print(count + 1)
            exit()
        if current_r != next_r or current_b != next_b:
            queue.append((count + 1, next_r, next_b))


print("-1")
