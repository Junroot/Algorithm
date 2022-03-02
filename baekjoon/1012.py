from sys import stdin

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
t = int(stdin.readline())

for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    positions = set()

    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        positions.add((x, y))


    def remove_adjacent_location(position):
        for direction in directions:
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if next_position in positions:
                positions.remove(next_position)
                remove_adjacent_location(next_position)


    result = 0
    while positions:
        position = positions.pop()
        result += 1
        remove_adjacent_location(position)

    print(result)
