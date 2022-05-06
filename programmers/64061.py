def solution(board, moves):
    board_size = len(board)
    count = 0

    columns = [[] for _ in range(board_size)]

    for x in range(board_size):
        for y in range(board_size - 1, -1, -1):
            if board[y][x] == 0:
                break
            columns[x].append(board[y][x])

    bucket = []

    for move in moves:
        if len(columns[move - 1]) == 0:
            continue
        picked_doll = columns[move - 1].pop()
        bucket.append(picked_doll)
        if len(bucket) >= 2:
            if bucket[-1] == bucket[-2]:
                bucket.pop()
                bucket.pop()
                count += 2

    return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))