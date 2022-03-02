import sys
from sys import stdin

sys.setrecursionlimit(10**6)

n = int(stdin.readline())
tree = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, stdin.readline().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))


def find_farthest_node(node):
    result = (0, node)
    visited[node] = True
    for next_node, weight in tree[node]:
        if not visited[next_node]:
            sub_result = find_farthest_node(next_node)
            if sub_result[0] + weight > result[0]:
                result = (sub_result[0] + weight, sub_result[1])
    return result


node = find_farthest_node(1)
visited = [False for _ in range(n + 1)]
print(find_farthest_node(node[1])[0])

