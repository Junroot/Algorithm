import sys
from collections import deque

n = int(sys.stdin.readline())
deque = deque()
deque.extend([i for i in range(1, n + 1)])

switch = False

while len(deque) > 1:
    number = deque.popleft()
    if switch:
        deque.append(number)
    switch = not switch

print(deque[0])
