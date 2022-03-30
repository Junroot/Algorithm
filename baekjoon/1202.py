from sys import stdin
import heapq

jewel_count, bag_count = map(int, stdin.readline().split())
jewels = [tuple(map(int, stdin.readline().split())) for _ in range(jewel_count)]
jewels.sort()
bags = [int(stdin.readline()) for _ in range(bag_count)]
bags.sort()

containable_jewels = []
jewel_index = 0
total_value = 0

for bag in bags:
    while jewel_index < jewel_count and jewels[jewel_index][0] <= bag:
        jewel_value = jewels[jewel_index][1]
        heapq.heappush(containable_jewels, -jewel_value)
        jewel_index += 1
    if containable_jewels:
        total_value -= heapq.heappop(containable_jewels)

print(total_value)
