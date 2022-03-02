from sys import stdin

n = int(stdin.readline())
triangle = [list(map(int, stdin.readline().split())) for _ in range(n)]
cache = [[triangle[0][0]]]

for i in range(1, len(triangle)):
    row = []
    for j in range(len(triangle[i])):
        if j == 0:
            row.append(cache[i - 1][j] + triangle[i][j])
        elif j == len(triangle[i]) - 1:
            row.append(cache[i - 1][j - 1] + triangle[i][j])
        else:
            row.append(max(cache[i - 1][j - 1], cache[i - 1][j]) + triangle[i][j])
    cache.append(row)

print(max(cache[-1]))
