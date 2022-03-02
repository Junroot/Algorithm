from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0 for _ in range(n + 1)]
q = deque([1])

while q:
    node = q.popleft()
    for next_node in graph[node]:
        if parents[next_node] != 0:
            continue
        parents[next_node] = node
        q.append(next_node)

for i in range(2, len(parents)):
    print(parents[i])
