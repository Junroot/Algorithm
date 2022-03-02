from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
counts = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    counts[b] += 1
    graph[a].append(b)


q = deque()

for i in range(1, n + 1):
    if counts[i] == 0:
        q.append(i)

result = []

while q:
    student = q.popleft()
    result.append(student)
    for next_student in graph[student]:
        counts[next_student] -= 1
        if counts[next_student] == 0:
            q.append(next_student)

print(" ".join(map(str, result)))
