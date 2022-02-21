from sys import stdin
from collections import deque

input = stdin.readline

v = int(input())
tree = [[] for _ in range(v + 1)]

for _ in range(v):
    edge_info = list(map(int, input().split()))
    parent = edge_info[0]
    for i in range(1, len(edge_info) - 1, 2):
        child = edge_info[i]
        weight = edge_info[i + 1]
        tree[parent].append((child, weight))
        tree[child].append((parent, weight))


def find_farthest_node(node):
    distances = [-1 for _ in range(v + 1)]
    distances[node] = 0
    q = deque([node])
    while q:
        now = q.popleft()
        for next, weight in tree[now]:
            if distances[next] == -1:
                distances[next] = distances[now] + weight
                q.append(next)
    max_distance = max(distances)
    return distances.index(max_distance), max_distance


print(find_farthest_node(find_farthest_node(1)[0])[1])
