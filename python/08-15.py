def is_not_duplicated(problem):
    counts = [0 for _ in range(10)]
    for char in problem:
        try:
            counts[int(char)] += 1
        except:
            pass
    return all(map(lambda count: count == 1, counts))


problems = input().split()

for problem in problems:
    print(is_not_duplicated(problem), end=" ")
