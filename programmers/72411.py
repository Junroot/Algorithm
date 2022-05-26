from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    order_count = defaultdict(int)
    for order in orders:
        order_count[''.join(sorted(order))] += 1

    course_count = [defaultdict(int) for _ in range(len(course))]

    for order in order_count.keys():
        for i, course_size in enumerate(course):
            for combination in combinations(order, course_size):
                course_count[i][''.join(combination)] += order_count[order]

    result = []

    for cc in course_count:
        max_count = 2
        courses = []
        for combination in cc:
            if cc[combination] > max_count:
                max_count = cc[combination]
                courses = [combination]
            elif cc[combination] == max_count:
                courses.append(combination)
        result.extend(courses)

    return sorted(result)


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
