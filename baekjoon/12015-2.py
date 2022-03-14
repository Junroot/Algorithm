n = int(input())
numbers = list(map(int, input().split()))
last_numbers = []

def find_lower_bound(numbers, lower_bound):
    start, end = 0, len(numbers)
    while start < end:
        mid = (end - start) // 2 + start
        if numbers[mid] < lower_bound:
            start = mid + 1
        else:
            end = mid
    return start


for number in numbers:
    if not last_numbers:
        last_numbers.append(number)
    elif last_numbers[-1] < number:
        last_numbers.append(number)
    else:
        last_numbers[find_lower_bound(last_numbers, number)] = number

print(len(last_numbers))


