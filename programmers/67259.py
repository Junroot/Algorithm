from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_valid_position(next_position, board_length):
    return 0 <= next_position[0] < board_length and 0 <= next_position[1] < board_length


def solution(board):
    cache = [[[25 * 25 * 500 for _ in range(4)] for _ in range(len(board))] for _ in range(len(board))]
    cache[0][0] = [0, 0, 0, 0]
    queue = deque([((0, 0), 0), ((0, 0), 1)])

    while queue:
        position, direction_index = queue.popleft()
        for next_direction_index, direction in enumerate(directions):
            now_cost = cache[position[1]][position[0]][direction_index]
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if not is_valid_position(next_position, len(board)):
                continue
            if board[next_position[1]][next_position[0]] == 1:
                continue

            if next_direction_index == direction_index:
                next_cost = now_cost + 100
            else:
                next_cost = now_cost + 600

            if next_cost < cache[next_position[1]][next_position[0]][next_direction_index]:
                cache[next_position[1]][next_position[0]][next_direction_index] = next_cost
                queue.append((next_position, next_direction_index))

    return min(cache[-1][-1])

solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
