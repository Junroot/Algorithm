from collections import deque

n = int(input())
times = [0 for _ in range(n + 1)]
next_lectures = [[] for _ in range(n + 1)]
essential_lecture_count = [0 for _ in range(n + 1)]

for lecture in range(1, n + 1):
    inputs = list(map(int, input().split()))
    times[lecture] = inputs[0]
    for essential_lecture in inputs[1:-1]:
        next_lectures[essential_lecture].append(lecture)
        essential_lecture_count[lecture] += 1

result = times[:]
q = deque()

for lecture in range(1, n + 1):
    if essential_lecture_count[lecture] == 0:
        q.append((times[lecture], lecture))

while q:
    time, essential_lecture = q.popleft()
    for lecture in next_lectures[essential_lecture]:
        result[lecture] = max(result[lecture], result[essential_lecture] + times[lecture])
        essential_lecture_count[lecture] -= 1
        if essential_lecture_count[lecture] == 0:
            q.append((times[lecture] + time, lecture))

for i in range(1, n + 1):
    print(result[i])



