from sys import stdin
import heapq

MAX_INT = 987654321
v, e = map(int, stdin.readline().split())
k = int(stdin.readline())
graph = [[] for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]
result = [MAX_INT for _ in range(v + 1)]

for _ in range(e):
    start, end, distance = map(int, stdin.readline().split())
    graph[start].append((end, distance))

result[k] = 0
q = [(0, k)]

while q:
    distance, now = heapq.heappop(q)
    if visited[now]:
        continue
    visited[now] = True
    for edge in graph[now]:
        if result[edge[0]] > distance + edge[1]:
            result[edge[0]] = distance + edge[1]
            heapq.heappush(q, (result[edge[0]], edge[0]))

for i in range(1, v + 1):
    if result[i] == MAX_INT:
        print("INF")
    else:
        print(result[i])
