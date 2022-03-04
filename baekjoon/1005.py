from collections import deque
from sys import stdin

number_of_case = int(stdin.readline())

for _ in range(number_of_case):

    building_count, rule_count = map(int, stdin.readline().split())
    times_of_buildings = [0] + list(map(int, stdin.readline().split()))
    children_of_buildings = [[] for _ in range(building_count + 1)]
    counts_of_depended_buildings = [0 for _ in range(building_count + 1)]
    maximum_times_of_buildings = [0 for _ in range(building_count + 1)]

    for _ in range(rule_count):
        parent, child = map(int, stdin.readline().split())
        children_of_buildings[parent].append(child)
        counts_of_depended_buildings[child] += 1

    target_building = int(stdin.readline())

    queue = deque()

    for i in range(1, building_count + 1):
        if counts_of_depended_buildings[i] == 0:
            queue.append((i, 0))

    building_count = 0

    while queue and building_count < building_count:
        building_index, time = queue.popleft()
        if building_index == target_building:
            print(time + times_of_buildings[building_index])
            break
        building_count += 1
        for child in children_of_buildings[building_index]:
            maximum_times_of_buildings[child] = max(maximum_times_of_buildings[child], time + times_of_buildings[building_index])
            counts_of_depended_buildings[child] -= 1
            if counts_of_depended_buildings[child] == 0:
                queue.append((child, maximum_times_of_buildings[child]))

