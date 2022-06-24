def solution(key, lock):
    def rotate(key):
        new_key = [[0 for _ in range(len(key))] for _ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key[0])):
                new_key[j][len(key) - i - 1] = key[i][j]
        return new_key

    keys = [key]
    for _ in range(3):
        keys.append(rotate(keys[-1]))

    def can_unlock(delta_x, delta_y, key):
        for y in range(len(lock)):
            for x in range(len(lock)):
                if delta_y > y or delta_x > x or y - delta_y >= len(key) or x - delta_x >= len(key):
                    if lock[y][x] == 0:
                        return False
                elif lock[y][x] == key[y - delta_y][x - delta_x]:
                    return False
        return True

    for y in range(1 - len(key), len(lock)):
        for x in range(1 - len(key), len(lock)):
            for key in keys:
                if can_unlock(x, y, key):
                    return True
    return False