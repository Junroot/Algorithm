n = int(input())
cache = [(0, 0), (0, 0)]

for x in range(2, n + 1):
    min_operation_count = cache[x - 1][0]
    previous_index = x - 1
    if x % 2 == 0 and min_operation_count > cache[x // 2][0]:
        min_operation_count = cache[x // 2][0]
        previous_index = x // 2
    if x % 3 == 0 and min_operation_count > cache[x // 3][0]:
        min_operation_count = cache[x // 3][0]
        previous_index = x // 3
    cache.append((min_operation_count + 1, previous_index))

route = [str(n)]
now_index = n

for _ in range(cache[n][0]):
    now_index = cache[now_index][1]
    route.append(str(now_index))

print(cache[n][0])
print(" ".join(route))
