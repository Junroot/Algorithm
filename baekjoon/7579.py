app_count, new_app_memory = map(int, input().split())
apps = []
cost_sum = 0

for memory in map(int, input().split()):
    apps.append([memory])

for i, cost in enumerate(map(int, input().split())):
    cost_sum += cost
    apps[i].append(cost)

cache = [[0 for _ in range(cost_sum + 1)] for _ in range(app_count)]

for i in range(apps[0][1], cost_sum + 1):
    cache[0][i] = apps[0][0]

result = 10000000

if apps[0][0] >= new_app_memory:
    result = apps[0][1]

for app_index in range(1, app_count):
    app_cost = apps[app_index][1]
    app_memory = apps[app_index][0]
    for cost in range(cost_sum + 1):
        cache[app_index][cost] = cache[app_index - 1][cost]
        if cost >= app_cost:
            cache[app_index][cost] = max(cache[app_index][cost], cache[app_index - 1][cost - app_cost] + app_memory)
        if cache[app_index][cost] >= new_app_memory:
            result = min(result, cost)

print(result)
