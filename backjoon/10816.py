import sys

n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
results = []


def find_lower_bound(number):
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if cards[mid] >= number:
            end = mid
        else:
            start = mid + 1
    return start


def find_upper_bound(number):
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if cards[mid] <= number:
            start = mid + 1
        else:
            end = mid
    return start


def count_number(number):
    return find_upper_bound(number) - find_lower_bound(number)


for number in numbers:
    results.append(str(count_number(number)))

print(" ".join(results))
