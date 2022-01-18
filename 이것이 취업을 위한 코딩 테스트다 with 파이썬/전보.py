import heapq

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    distances = [INF for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        distance, now = heapq.heappop(q)
        if distances[now] < distance:
            continue
        distances[now] = distance
        for destination, edge in graph[now]:
            heapq.heappush(q, (distance + edge, destination))
    return distances


distances_from_c = dijkstra(c)
max = -1
count = 0
for i in range(1, len(distances_from_c)):
    if distances_from_c[i] >= INF:
        continue
    count += 1
    if distances_from_c[i] > max:
        max = distances_from_c[i]

print(count - 1, max)
