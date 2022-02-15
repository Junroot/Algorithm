n = int(input())
numbers = list(map(int, input().split()))
cache = dict()


def find_max_len(index, current_number):
    if index >= n:
        return 0
    if (index, current_number) in cache:
        return cache[(index, current_number)]
    result = find_max_len(index + 1, current_number)
    if numbers[index] > current_number:
        result = max(1 + find_max_len(index + 1, numbers[index]), result)
    cache[(index, current_number)] = result
    return result


print(find_max_len(0, -1))
