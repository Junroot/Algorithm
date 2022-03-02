import sys

n = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))

start = 0
end = n - 1

minimum = 20000000001
result = None

while start < end:
    summation = solutions[start] + solutions[end]
    abs_summation = abs(summation)
    if minimum > abs_summation:
        minimum = abs_summation
        result = (start, end)
    if summation < 0:
        start += 1
    elif summation > 0:
        end -= 1
    else:
        break

print(str(solutions[result[0]]) + " " + str(solutions[result[1]]))
