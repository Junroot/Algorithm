MAX_INT = 160000000

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j and graph[i][j] == 0:
            graph[i][j] = MAX_INT

cache = [[MAX_INT for _ in range(1 << n)] for _ in range(n)]


def dfs(node, visited):
    if visited == (1 << n) - 1:
        return graph[node][0]

    if cache[node][visited] != MAX_INT:
        return cache[node][visited]

    for i in range(n):
        if node == i:
            continue
        if (visited >> i) % 2:
            continue

        new_visited = visited | (1 << i)
        cache[node][visited] = min(cache[node][visited], dfs(i, new_visited) + graph[node][i])
    return cache[node][visited]


print(dfs(0, 1))
