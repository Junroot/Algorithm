def check(delta_x, delta_y, key, lock):
    m = len(key)
    n = len(lock)

    for x in range(0, n):
        for y in range(0, n):
            if 0 <= x + delta_x < m and 0 <= y + delta_y < m:
                if key[y + delta_y][x + delta_x] + lock[y][x] != 1:
                    return False
            elif lock[y][x] != 1:
                return False

    return True


def rotate(key):
    result = [[0 for _ in range(len(key))] for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            result[j][len(key) - 1 - i] = key[i][j]
    return result


def solution(key, lock):
    m = len(key)
    n = len(lock)

    for _ in range(4):
        for delta_y in range(m - 1, -n, -1):
            for delta_x in range(m - 1, -n, -1):
                if check(delta_x, delta_y, key, lock):
                    return True
        key = rotate(key)
    return False
