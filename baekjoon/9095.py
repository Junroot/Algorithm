from collections import deque
from sys import stdin

results = [0, 1, 2, 4]

for n in range(4, 11):
    results.append(results[n - 3] + results[n - 2] + results[n - 1])

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(results[n])
