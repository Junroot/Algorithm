from collections import deque
from sys import stdin

input = stdin.readline

board_size, passenger_count, fuel = map(int, input().split())
board = [[1 for _ in range(board_size + 1)]]
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for _ in range(board_size):
    board.append([1] + list(map(int, input().split())))

driver = tuple(map(int, input().split()))
passengers = [[None for _ in range(board_size + 1)] for _ in range(board_size + 1)]

for _ in range(passenger_count):
    start_row, start_column, end_row, end_column = map(int, input().split())
    passengers[start_row][start_column] = (end_row, end_column)


def is_valid_position(row, column):
    return 1 <= row <= board_size and 1 <= column <= board_size


def find_nearest_passenger():
    queue = deque([driver])
    visited = [[False for _ in range(board_size + 1)] for _ in range(board_size + 1)]
    visited[driver[0]][driver[1]] = True
    distance = 0
    while queue:
        queue_length = len(queue)
        results = []
        for _ in range(queue_length):
            now_row, now_column = queue.popleft()
            if passengers[now_row][now_column] is not None:
                results.append((now_row, now_column))
            for direction in directions:
                next_row = now_row + direction[0]
                next_column = now_column + direction[1]
                if is_valid_position(next_row, next_column) and board[next_row][next_column] != 1 and not \
                        visited[next_row][next_column]:
                    queue.append((next_row, next_column))
                    visited[next_row][next_column] = True
        if len(results) != 0:
            results.sort()
            return distance, results[0]
        distance += 1
    return -1, None


def get_distance(destination):
    queue = deque([driver])
    visited = [[False for _ in range(board_size + 1)] for _ in range(board_size + 1)]
    visited[driver[0]][driver[1]] = True
    distance = 0
    while queue:
        queue_length = len(queue)
        for _ in range(queue_length):
            now_row, now_column = queue.popleft()
            if (now_row, now_column) == destination:
                return distance
            for direction in directions:
                next_row = now_row + direction[0]
                next_column = now_column + direction[1]
                if is_valid_position(next_row, next_column) and board[next_row][next_column] != 1 and not \
                        visited[next_row][next_column]:
                    queue.append((next_row, next_column))
                    visited[next_row][next_column] = True
        distance += 1
    return -1


for _ in range(passenger_count):
    distance, passenger_position = find_nearest_passenger()
    if distance == -1:
        print(-1)
        exit()
    if distance > fuel:
        print(-1)
        exit()
    fuel -= distance
    driver = passenger_position
    distance = get_distance(passengers[passenger_position[0]][passenger_position[1]])
    if distance == -1:
        print(-1)
        exit()
    if distance > fuel:
        print(-1)
        exit()
    fuel = fuel + distance
    driver = passengers[passenger_position[0]][passenger_position[1]]
    passengers[passenger_position[0]][passenger_position[1]] = None

print(fuel)
