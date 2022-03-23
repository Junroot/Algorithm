def is_prime(partial_number):
    if partial_number < 2:
        return False
    for i in range(2, int(partial_number ** 0.5) + 1):
        if partial_number % i == 0:
            return False
    return True


def solution(n, k):
    number = 0

    while n > 0:
        number *= 10
        number += n % k
        n //= k

    number = str(number)[::-1]
    partial_number = 0

    result = 0
    for i in range(len(number)):
        if number[i] == "0":
            if is_prime(partial_number):
                result += 1
            partial_number = 0
        partial_number *= 10
        partial_number += int(number[i])
    if is_prime(partial_number):
        result += 1
    return result


print(solution(11011, 10))
