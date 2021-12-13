import functools


def compare(number1, number2):
    concat1, concat2 = number1 + number2, number2 + number1
    if concat1 > concat2:
        return -1
    if concat1 == concat2:
        return 0
    return 1


def solution(numbers):
    converted_numbers = list(map(str, numbers))
    converted_numbers.sort(key=functools.cmp_to_key(compare))
    return str(int("".join(converted_numbers)))

