def solution(n, s, a, b, fares):
    max_int = 987654321

    board = [[max_int for _ in range(n + 1)] for _ in range(n + 1)]

    for fare in fares:
        board[fare[0]][fare[1]] = fare[2]
        board[fare[1]][fare[0]] = fare[2]

    for i in range(n + 1):
        board[i][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                board[j][k] = min(board[j][k], board[j][i] + board[i][k])

    answer = max_int
    for i in range(1, n + 1):
        answer = min(answer, board[s][i] + board[i][a] + board[i][b])
    return answer

