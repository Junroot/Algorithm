from sys import stdin

n = int(stdin.readline())
meetings = []

for _ in range(n):
    start, end = map(int, stdin.readline().split())
    meetings.append((start, end))

meetings.sort(key=lambda meeting: (meeting[1], meeting[0]))

count = 0
time = 0

for meeting in meetings:
    if meeting[0] < time:
        continue
    count += 1
    time = meeting[1]

print(count)
