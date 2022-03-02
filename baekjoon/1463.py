from collections import deque

q = deque()
x = int(input())
visited = set()
q.append((1, 0))

while q:
    data = q.popleft()
    if data[0] > x:
        continue
    if data[0] in visited:
        continue
    if data[0] == x:
        print(data[1])
        break
    visited.add(data[0])
    q.append((data[0] * 3, data[1] + 1))
    q.append((data[0] * 2, data[1] + 1))
    q.append((data[0] + 1, data[1] + 1))
