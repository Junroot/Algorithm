from sys import stdin
from collections import deque, defaultdict

test_case = int(stdin.readline())

for _ in range(test_case):
    height, width = map(int, stdin.readline().split())
    board = [list(stdin.readline().rstrip()) for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]

    points_to_visit = deque()
    waited_doors = defaultdict(list)

    keys = set(stdin.readline().rstrip())
    if "0" in keys:
        keys = set()


    def visit(column, row):
        points_to_visit.append((column, row))
        visited[row][column] = True

    docs_count = 0


    def initialize():
        global docs_count
        for row in range(height):
            for column in range(width):
                if row == 0 or column == 0 or row == height - 1 or column == width - 1:
                    point = board[row][column]
                    if point == ".":
                        visit(column, row)
                    elif "a" <= point <= "z":
                        visit(column, row)
                        keys.add(point)
                    elif "A" <= point <= "Z":
                        waited_doors[point.lower()].append((column, row))
                    elif point == "$":
                        docs_count += 1
                        visit(column, row)


    def open_doors(key):
        if len(waited_doors[key]) != 0:
            for column, row in waited_doors[key]:
                visit(column, row)
            waited_doors[key] = []


    def next_points(column, row):
        result = []
        if column > 0:
            result.append((column - 1, row))
        if column < width - 1:
            result.append((column + 1, row))
        if row > 0:
            result.append((column, row - 1))
        if row < height - 1:
            result.append((column, row + 1))
        return result


    initialize()
    for key in keys:
        open_doors(key)

    while points_to_visit:
        column, row = points_to_visit.popleft()
        for next_column, next_row in next_points(column, row):
            if visited[next_row][next_column]:
                continue
            point = board[next_row][next_column]
            if point == ".":
                visit(next_column, next_row)
            elif "a" <= point <= "z":
                visit(next_column, next_row)
                keys.add(point)
                open_doors(point)
            elif "A" <= point <= "Z":
                if point.lower() in keys:
                    visit(next_column, next_row)
                else:
                    waited_doors[point.lower()].append((column, row))
            elif point == "$":
                docs_count += 1
                visit(next_column, next_row)

    print(docs_count)
