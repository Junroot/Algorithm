import heapq


def solution(n, edge):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    distances = [INF for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        distance, now = heapq.heappop(q)
        if distances[now] <= distance:
            continue
        distances[now] = distance
        for destination in graph[now]:
            heapq.heappush(q, (distance + 1, destination))

    max_length = -1
    count = 0
    for d in distances:
        if d >= INF:
            continue
        if d > max_length:
            max_length = d
            count = 1
        elif d == max_length:
            count += 1
    return count


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
