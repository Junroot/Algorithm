def solution(number, k):
    return select_digit(number, len(number) - k)


def select_digit(number, k):
    result = ""
    min_selectable_index = 0
    max_selectable_index = len(number) - k + 1
    while k > 0:
        max_digit = number[min_selectable_index]
        max_index = min_selectable_index
        for i in range(min_selectable_index, max_selectable_index):
            if max_digit == "9":
                break
            digit = number[i]
            if digit > max_digit:
                max_digit = digit
                max_index = i
        result += max_digit
        min_selectable_index = max_index + 1
        max_selectable_index += 1
        k -= 1
    return result
