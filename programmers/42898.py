def solution(m, n, puddles):
    map = [[0] * m for _ in range(n)]
    map[0][0] = 1
    for puddle in puddles:
        map[puddle[1] - 1][puddle[0] - 1] = -1

    for i in range(1, m + n - 1):
        for y in range(min(i + 1, n)):
            x = i - y
            if x >= m:
                continue
            if map[y][x] == -1:
                map[y][x] = 0
                continue
            up = 0
            if y > 0:
                up = map[y - 1][x]
            left = 0
            if x > 0:
                left = map[y][x - 1]
            map[y][x] = (up + left) % 1000000007
    return map[n - 1][m - 1]
