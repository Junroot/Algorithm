import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    company1, company2 = map(int, input().split())
    graph[company1][company2] = 1
    graph[company2][company1] = 1
x, k = map(int, input().split())

for mid in range(1, n + 1):
    for source in range(1, n + 1):
        for destination in range(1, n + 1):
            graph[source][destination] = min(graph[source][destination], graph[source][mid] + graph[mid][destination])

result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)
