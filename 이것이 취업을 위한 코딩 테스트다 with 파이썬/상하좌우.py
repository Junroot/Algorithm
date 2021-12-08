n = int(input())
directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
movements = input().split()
current_point = (1, 1)


def is_possible_point(point, n):
    return 0 < point[0] <= n and 0 < point[1] <= n


def next_point(m, c_p):
    direction = directions[m]
    return c_p[0] + direction[0], c_p[1] + direction[1]


for movement in movements:
    n_point = next_point(movement, current_point)
    if is_possible_point(n_point, n):
        current_point = n_point

print(current_point[0], current_point[1])
