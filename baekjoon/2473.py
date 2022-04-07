solution_count = int(input())
solutions = sorted(map(int, input().split()))

min_acidity = 3000000000
result = None

for pivot_index in range(solution_count - 2):
    start, end = pivot_index + 1, solution_count - 1
    while start < end:
        acidity = solutions[pivot_index] + solutions[start] + solutions[end]
        if min_acidity > abs(acidity):
            min_acidity = abs(acidity)
            result = (solutions[pivot_index], solutions[start], solutions[end])
        if acidity < 0:
            start += 1
        elif acidity > 0:
            end -= 1
        else:
            break

print(*result)
