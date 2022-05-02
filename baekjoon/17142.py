from collections import deque
from itertools import permutations, combinations

size_of_room, virus_count = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(size_of_room)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

blank_count = 0
viruses = []

for y in range(size_of_room):
    for x in range(size_of_room):
        if room[y][x] == 2:
            viruses.append((y, x))
        elif room[y][x] == 0:
            blank_count += 1


def calculate_time(viruses_queue):
    time = 0
    transmit_count = 0
    test_room = [[room[y][x] for x in range(size_of_room)] for y in range(size_of_room)]
    for virus in viruses_queue:
        test_room[virus[0]][virus[1]] = 3
    while viruses_queue:
        viruses_queue_length = len(viruses_queue)
        if transmit_count == blank_count:
            break
        for _ in range(viruses_queue_length):
            y, x = viruses_queue.popleft()
            for direction in directions:
                new_y = y + direction[0]
                new_x = x + direction[1]
                if 0 <= new_y < size_of_room and 0 <= new_x < size_of_room:
                    if test_room[new_y][new_x] == 0:
                        test_room[new_y][new_x] = 3
                        transmit_count += 1
                        viruses_queue.append((new_y, new_x))
                    elif test_room[new_y][new_x] == 2:
                        test_room[new_y][new_x] = 3
                        viruses_queue.append((new_y, new_x))
        time += 1

    if transmit_count == blank_count:
        return time
    else:
        return -1


cache = [[None for _ in range(2500)] for _ in range(11)]


def get_all_combinations(count, start_index):
    if count == 0:
        return [[]]
    if cache[count][start_index] is not None:
        return cache[count][start_index]
    result = []
    for i in range(start_index, len(viruses) - count + 1):
        sub_results = get_all_combinations(count - 1, i + 1)
        for sub_result in sub_results:
            result.append([i] + sub_result)
    cache[count][start_index] = result
    return result


result_time = 987654321
active_virus_combinations = combinations(viruses, r=virus_count)
for combination in active_virus_combinations:
    time = calculate_time(deque(combination))
    if time != -1:
        result_time = min(result_time, time)

if result_time != 987654321:
    print(result_time)
else:
    print(-1)
