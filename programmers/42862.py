def solution(n, lost, reserve):
    lost, reserve = initialize(lost, reserve)
    answer = n - len(lost)
    for lost_student in lost:
        if can_borrow_from_left(lost_student, reserve):
            reserve.remove(lost_student - 1)
            answer += 1
        elif can_borrow_from_right(lost_student, reserve, n):
            reserve.remove(lost_student + 1)
            answer += 1
    return answer


def initialize(lost, reserve):
    new_lost, new_reserve = lost[:], reserve[:]
    for lost_element in lost:
        if lost_element in reserve:
            new_lost.remove(lost_element)
            new_reserve.remove(lost_element)
    new_lost.sort()
    new_reserve.sort()
    return new_lost, new_reserve


def can_borrow_from_left(student, reserve):
    if student == 1:
        return False
    return student - 1 in reserve


def can_borrow_from_right(student, reserve, n):
    if student == n:
        return False
    return student + 1 in reserve
