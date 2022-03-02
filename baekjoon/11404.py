from sys import stdin

INF = 1e10

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
