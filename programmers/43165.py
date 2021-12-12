def solution(numbers, target):
    if len(numbers) == 0:
        if target == 0:
            return 1
        return 0
    number = numbers[-1]

    return solution(numbers[:-1], target - number) + solution(numbers[:-1], target + number)


print(solution([1, 1, 1, 1, 1], 3))
