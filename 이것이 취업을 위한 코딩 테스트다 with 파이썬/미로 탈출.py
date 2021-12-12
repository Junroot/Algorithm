from collections import deque


def is_possible_point(point, m, n):
    return 0 <= point[0][0] < m and 0 <= point[0][1] < n


def find_min_movement_count(maze, m, n):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    queue = deque([((0, 0), 1)])
    while queue:
        now_point = queue.popleft()
        maze[now_point[0][1]][now_point[0][0]] = "0"
        if now_point[0][0] == m - 1 and now_point[0][1] == n - 1:
            return now_point[1]
        for direction in directions:
            new_point = ((now_point[0][0] + direction[0], now_point[0][1] + direction[1]), now_point[1] + 1)
            if is_possible_point(new_point, m, n) and maze[new_point[0][1]][new_point[0][0]] == "1":
                queue.append(new_point)


n, m = map(int, input().split())
maze = []


for i in range(n):
    maze.append(list(input()))


print(find_min_movement_count(maze, m, n))

