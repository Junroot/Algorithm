def solution(n, arr1, arr2):
    board = []
    for i in range(len(arr1)):
        bitmap = arr1[i] | arr2[i]
        row = ""
        for j in range(n):
            if bitmap % 2 == 1:
                row += "#"
            else:
                row += " "
            bitmap //= 2
        board.append(row[::-1])

    return board
