from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_next_positions(feet, board):
    result = get_shifted_positions(feet, board)
    result.extend(get_rotated_positions(feet, board))
    return result


def get_shifted_positions(feet, board):
    result = []
    for direction in directions:
        next_feet = []
        for foot in feet:
            next_feet.append((direction[0] + foot[0], direction[1] + foot[1]))
        next_feet.sort()
        if is_valid_feet(board, next_feet):
            result.append(next_feet)
    return result


def get_rotated_positions(feet, board):
    result = []
    if feet[0][0] == feet[1][0]:
        if is_valid_feet(board, [(feet[0][0] - 1, feet[0][1]), (feet[1][0] - 1, feet[1][1])]):
            result.append([(feet[1][0] - 1, feet[1][1]), (feet[1][0], feet[1][1])])
            result.append([(feet[0][0] - 1, feet[0][1]), (feet[0][0], feet[0][1])])
        if is_valid_feet(board, [(feet[0][0] + 1, feet[0][1]), (feet[1][0] + 1, feet[1][1])]):
            result.append([(feet[1][0], feet[1][1]), (feet[1][0] + 1, feet[1][1])])
            result.append([(feet[0][0], feet[0][1]), (feet[0][0] + 1, feet[0][1])])
    else:
        if is_valid_feet(board, [(feet[0][0], feet[0][1] - 1), (feet[1][0], feet[1][1] - 1)]):
            result.append([(feet[1][0], feet[1][1] - 1), (feet[1][0], feet[1][1])])
            result.append([(feet[0][0], feet[0][1] - 1), (feet[0][0], feet[0][1])])
        if is_valid_feet(board, [(feet[0][0], feet[0][1] + 1), (feet[1][0], feet[1][1] + 1)]):
            result.append([(feet[1][0], feet[1][1]), (feet[1][0], feet[1][1] + 1)])
            result.append([(feet[0][0], feet[0][1]), (feet[0][0], feet[0][1] + 1)])
    return result


def is_valid_feet(board, feet):
    for foot in feet:
        if not is_valid_foot(board, foot):
            return False
    return True


def is_valid_foot(board, foot):
    if 0 > foot[0] or len(board) <= foot[0] or 0 > foot[1] or len(board) <= foot[1]:
        return False
    if board[foot[0]][foot[1]] == 1:
        return False
    return True


def get_hash_code(feet, n):
    result = 0
    for foot in feet:
        for i in range(2):
            result *= n
            result += foot[i]
    return result


def solution(board):
    queue = deque([[(0, 0), (0, 1)]])
    n = len(board)
    visited = set()
    visited.add(get_hash_code([(0, 0), (0, 1)], n))
    count = 0
    while queue:
        length = len(queue)
        for _ in range(length):
            feet = queue.popleft()
            for foot in feet:
                if foot == (n - 1, n - 1):
                    return count
            for next_position in get_next_positions(feet, board):
                hash_code = get_hash_code(next_position, n)
                if hash_code not in visited:
                    visited.add(hash_code)
                    queue.append(next_position)
        count += 1
    return -1
