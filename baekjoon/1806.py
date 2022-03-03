from collections import deque

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
result = 1000001
queue = deque()
sum = 0

for number in numbers:
    queue.append(number)
    sum += number

    while sum - queue[0] >= s:
        thrown_number = queue.popleft()
        sum -= thrown_number

    if sum >= s:
        result = min(result, len(queue))

if result == 1000001:
    print(0)
else:
    print(result)

