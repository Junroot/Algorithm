from sys import stdin
from collections import deque

movements = [(-1, 0), (0, -1), (1, 0), (0, 1)]

n, m = map(int, stdin.readline().split())
maze = [stdin.readline().rstrip() for _ in range(n)]
visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
q = deque([(1, 0, (0, 0))])


def is_valid_position(position):
    return 0 <= position[0] < m and 0 <= position[1] < n


while q:
    distance, chance_count, position = q.popleft()
    if position == (m - 1, n - 1):
        print(distance)
        exit()
    for movement in movements:
        next_position = (position[0] + movement[0], position[1] + movement[1])
        if not is_valid_position(next_position):
            continue
        if visited[next_position[1]][next_position[0]][chance_count]:
            continue
        if maze[next_position[1]][next_position[0]] == "1" and chance_count == 0:
            visited[next_position[1]][next_position[0]][1] = True
            q.append((distance + 1, 1, next_position))
        if maze[next_position[1]][next_position[0]] == "0":
            visited[next_position[1]][next_position[0]][chance_count] = True
            q.append((distance + 1, chance_count, next_position))

print(-1)
