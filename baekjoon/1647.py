n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()


def find_group(house):
    parent = parents[house]
    while parent != parents[parent]:
        parent = parents[parent]
    parents[house] = parent
    return parent


def is_same_group(house1, house2):
    return find_group(house1) == find_group(house2)


def merge_group(house1, house2):
    group1 = find_group(house1)
    group2 = find_group(house2)
    if group1 < group2:
        parents[group2] = group1
    elif group2 < group1:
        parents[group1] = group2


count = 0
cost = 0
max_cost = 0

for edge in edges:
    c, a, b = edge
    if not is_same_group(a, b):
        merge_group(a, b)
        cost += c
        count += 1
        max_cost = c
        if count == n - 1:
            break

print(cost - max_cost)
