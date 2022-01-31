import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())
    operator = command[0]

    if operator == "push":
        q.append(command[1])
    elif operator == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif operator == "size":
        print(len(q))
    elif operator == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif operator == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])

