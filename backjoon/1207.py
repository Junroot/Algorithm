from sys import stdin, stdout

L = int(stdin.readline())
pieces = []
board = [[0 for _ in range(L)] for _ in range(L)]
count = 0

for id in range(1, 6):
    height, width = map(int, stdin.readline().split())
    piece = []
    for _ in range(height):
        row = list(map(lambda x: id if x == '#' else 0, stdin.readline().rstrip()))
        count += sum(map(lambda x: x != 0, row))
        piece.append(row)
    pieces.append(piece)

if count != L ** 2:
    print("gg")
    exit()


def can_put_piece(i, x, y):
    piece = pieces[i]
    for j in range(len(piece)):
        for k in range(len(piece[0])):
            if piece[j][k] != 0 and board[y + j][x + k] != 0:
                return False
    return True


def put_piece(i, x, y):
    piece = pieces[i]
    for j in range(len(piece)):
        for k in range(len(piece[0])):
            board[y + j][x + k] += piece[j][k]


def unput_piece(i, x, y):
    piece = pieces[i]
    for j in range(len(piece)):
        for k in range(len(piece[0])):
            board[y + j][x + k] -= piece[j][k]


def can_arrange(i):
    if i == 5:
        return True
    piece = pieces[i]
    for j in range(L - len(piece) + 1):
        for k in range(L - len(piece[0]) + 1):
            if can_put_piece(i, k, j):
                put_piece(i, k, j)
                if can_arrange(i + 1):
                    return True
                unput_piece(i, k, j)
    return False


if can_arrange(0):
    for i in range(L):
        stdout.write("".join(map(lambda x: str(x), board[i])) + "\n")
else:
    print("gg")
