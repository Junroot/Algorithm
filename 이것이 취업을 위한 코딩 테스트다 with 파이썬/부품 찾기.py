def exists(start, end, data, parts):
    while end >= start:
        mid = (start + end) // 2
        if parts[mid] == data:
            return True
        elif parts[mid] > data:
            end = mid - 1
        else:
            start = mid + 1
    return False


n = int(input())
parts = list(map(int, input().split()))
parts.sort()
m = int(input())
parts_to_find = list(map(int, input().split()))

for part_to_find in parts_to_find:
    if exists(0, len(parts) - 1, part_to_find, parts):
        print("yes", end=" ")
    else:
        print("no", end=" ")

