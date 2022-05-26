from collections import defaultdict


def count_satisfied_grades(grades, min_grade):
    start = 0
    end = len(grades)
    while start < end:
        mid = (start + end) // 2
        if grades[mid] < min_grade:
            start = mid + 1
        else:
            end = mid
    return len(grades) - end


def solution(info, query):
    grades = defaultdict(list)
    for person in info:
        language, part, career, food, grade = person.split()
        grade = int(grade)
        grades["".join([language, part, career, food])].append(grade)

    for characteristic in grades:
        grades[characteristic].sort()

    answer = []

    for q in query:
        language, part, career, food_grade = q.split(" and ")
        food, grade = food_grade.split()
        grade = int(grade)

        if language == "-":
            languages = ["cpp", "java", "python"]
        else:
            languages = [language]

        if part == "-":
            parts = ["backend", "frontend"]
        else:
            parts = [part]

        if career == "-":
            careers = ["junior", "senior"]
        else:
            careers = [career]

        if food == "-":
            foods = ["chicken", "pizza"]
        else:
            foods = [food]

        total = 0
        for l in languages:
            for p in parts:
                for c in careers:
                    for f in foods:
                        total += count_satisfied_grades(grades["".join([l, p, c, f])], grade)

        answer.append(total)
    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
