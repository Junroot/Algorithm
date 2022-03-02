from sys import stdin

n, m = map(int, stdin.readline().split())
table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, stdin.readline().split()))
    for j in range(1, n + 1):
        table[i][j] = row[j - 1]

inputs = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, n + 1):
        row_sum += table[i][j]
        table[i][j] = table[i - 1][j] + row_sum

results = []

for x1, y1, x2, y2 in inputs:
    results.append(table[x2][y2] - table[x2][y1 - 1] - table[x1 - 1][y2] + table[x1 - 1][y1 - 1])

print("\n".join(map(str, results)))
