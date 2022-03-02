import sys

n = int(sys.stdin.readline())
points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    points.append((x, y))

points.sort()

for point in points:
    print(str(point[0]) + " " + str(point[1]))
