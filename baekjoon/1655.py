import heapq
from sys import stdin

n = int(stdin.readline())
max_pq = []
min_pq = []


def balance():
    difference = len(max_pq) - len(min_pq)
    while difference < 0 or difference > 1:
        if difference > 1:
            heapq.heappush(min_pq, -heapq.heappop(max_pq))
            difference -= 1
        else:
            heapq.heappush(max_pq, -heapq.heappop(min_pq))
            difference += 1


for _ in range(n):
    number = int(stdin.readline())
    if not max_pq or -number >= max_pq[0]:
        heapq.heappush(max_pq, -number)
    else:
        heapq.heappush(min_pq, number)
    balance()
    print(-max_pq[0])
