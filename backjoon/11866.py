from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
numbers = deque([str(i) for i in range(1, n + 1)])
result = []

for _ in range(n):
    for _ in range(k - 1):
        number = numbers.popleft()
        numbers.append(number)
    result.append(numbers.popleft())

print("<" + ", ".join(result) + ">")
