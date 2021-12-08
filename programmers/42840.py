def solution(answers):
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    grades = []
    for pattern in patterns:
        grade = 0
        for problem_number in range(len(answers)):
            if pattern[problem_number % len(pattern)] == answers[problem_number]:
                grade += 1
        grades.append(grade)

    max_grade = max(grades)
    result = []
    for i in range(len(grades)):
        if max_grade == grades[i]:
            result.append(i + 1)
    return result
