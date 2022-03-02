import heapq

MAX_POSITION = 100000

n, k = map(int, input().split())
visited = [False for _ in range(1000001)]
pq = [(0, n)]

while pq:
    time, position = heapq.heappop(pq)
    if position == k:
        print(time)
        break
    if visited[position]:
        continue
    visited[position] = True
    if position * 2 <= MAX_POSITION:
        heapq.heappush(pq, (time, position * 2))
    if position - 1 >= 0:
        heapq.heappush(pq, (time + 1, position - 1))
    if position + 1 <= MAX_POSITION:
        heapq.heappush(pq, (time + 1, position + 1))
