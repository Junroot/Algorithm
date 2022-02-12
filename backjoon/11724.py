from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)


def bfs(node):
    q = deque([node])
    while q:
        now = q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        q.extend(graph[now])


count = 0
for node in range(1, n + 1):
    if not visited[node]:
        bfs(node)
        count += 1

print(count)
