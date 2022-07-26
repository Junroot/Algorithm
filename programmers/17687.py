def convert(number, base):
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        r = number % base
        if r >= 10:
            result += chr(ord('A') + r - 10)
        else:
            result += str(r)
        number //= base
    return result[::-1]


def solution(n, t, m, p):
    number = 0
    index = 0
    next_p = p - 1
    answer = ""
    while len(answer) < t:
        string = convert(number, n)
        for char in string:
            if index == next_p:
                answer += char
                next_p += m
                if len(answer) == t:
                    return answer
            index += 1
        number += 1
    return answer

solution(2, 4, 2, 1)
