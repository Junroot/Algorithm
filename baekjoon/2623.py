from sys import stdin
from collections import deque

singer_count, pd_count = map(int, stdin.readline().split())
graph = [[] for _ in range(singer_count + 1)]
previous_singer_counts = [0 for _ in range(singer_count + 1)]

for _ in range(pd_count):
    singer_order = list(map(int, stdin.readline().split()))
    for i in range(1, singer_order[0]):
        current_singer = singer_order[i]
        next_singer = singer_order[i + 1]
        graph[current_singer].append(next_singer)
        previous_singer_counts[next_singer] += 1

left_singer = singer_count
result_order = []
queue = deque()

for i in range(1, len(previous_singer_counts)):
    previous_singer_count = previous_singer_counts[i]
    if previous_singer_count == 0:
        queue.append(i)

while queue:
    singer = queue.popleft()
    result_order.append(singer)
    left_singer -= 1
    for next_singer in graph[singer]:
        previous_singer_counts[next_singer] -= 1
        if previous_singer_counts[next_singer] == 0:
            queue.append(next_singer)

if left_singer == 0:
    print("\n".join(map(str, result_order)))
else:
    print("0")

