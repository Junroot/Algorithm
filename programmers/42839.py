import math


def get_primes(max_number):
    primes = []
    for i in range(2, max_number + 1):
        is_prime = True
        square = round(math.sqrt(i)) + 1
        for prime in primes:
            if prime > square:
                break
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


def is_prime(primes, number):
    start = 0
    end = len(primes) - 1
    while start <= end:
        mid = (start + end) // 2
        prime = primes[mid]
        if prime < number:
            start = mid + 1
        elif prime > number:
            end = mid - 1
        else:
            return True
    return False


def get_permutations(digits):
    if len(digits) == 0:
        return [""]
    result = []
    for i in range(len(digits)):
        tails = get_permutations(digits[:i] + digits[i + 1:])
        for tail in tails:
            result.append(digits[i] + tail)
            result.append(tail)
    return result


def solution(numbers):
    permutations = set(map(int, filter(lambda x: x, get_permutations(numbers))))
    primes = get_primes(max(permutations))
    result = []

    for comb in permutations:
        if not comb:
            continue
        number = int(comb)
        if is_prime(primes, number):
            result.append(number)
    return len(result)


print(solution("17"))
print(solution("011"))
