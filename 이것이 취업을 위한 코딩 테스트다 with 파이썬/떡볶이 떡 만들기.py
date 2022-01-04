def get_rice_cake_length(array, cutter_length):
    rice_cake_length = 0
    for element in array:
        if element > cutter_length:
            rice_cake_length += element - cutter_length
    return rice_cake_length


def binary_search(array, target):
    start, end = 0, array[len(array) - 1]
    while end >= start:
        mid = (start + end) // 2
        rice_cake_length = get_rice_cake_length(array, mid)
        if rice_cake_length == target:
            return mid
        elif rice_cake_length > target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))
rice_cakes.sort()

print(binary_search(rice_cakes, m))
