from collections import deque
from sys import stdin

number_of_computers = int(stdin.readline())
number_of_edges = int(stdin.readline())
graph = [[] for _ in range(number_of_computers + 1)]

for _ in range(number_of_edges):
    first_computer, second_computer = map(int, stdin.readline().split())
    graph[first_computer].append(second_computer)
    graph[second_computer].append(first_computer)

visited = [False for _ in range(number_of_computers + 1)]

q = deque()
q.append(1)
result = 0

while q:
    node = q.popleft()
    if visited[node]:
        continue
    visited[node] = True
    result += 1
    q.extend(graph[node])

print(result - 1)
