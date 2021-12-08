def turn_left(now_d):
    return (now_d + 3) % 4


def go_straight(now_d, now_p):
    direction = directions[now_d]
    return now_p[0] + direction[0], now_p[1] + direction[1]


def go_back(now_d, now_p):
    direction = directions[now_d]
    return now_p[0] - direction[0], now_p[1] - direction[1]


def possible_point(p, n, m):
    return 0 <= p[0] < m and 0 <= p[1] < n


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
n, m = list(map(int, input().split()))
p_x, p_y, d = list(map(int, input().split()))
p = (p_x, p_y)
game_map = []

for i in range(n):
    game_map.append(list(map(int, input().split())))

count = 1
game_map[p_y][p_x] = 1

while True:
    success = False
    for _ in range(4):
        d = turn_left(d)
        next_p = go_straight(d, p)
        if possible_point(next_p, n, m) and game_map[next_p[1]][next_p[0]] == 0:
            p = next_p
            count += 1
            success = True
            game_map[next_p[1]][next_p[0]] = 2
            break
    if success:
        continue
    next_p = go_back(d, p)
    if not possible_point(next_p, n, m) or game_map[next_p[1]][next_p[0]] == 1:
        break
    p = next_p

print(count)
