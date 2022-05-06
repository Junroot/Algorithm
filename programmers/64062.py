import heapq
from collections import defaultdict


def solution(stones, k):
    stone_group = defaultdict(int)
    stone_type = []
    max_stone_in_group = 0
    for stone in stones[:k]:
        stone_group[stone] += 1
        if stone_group[stone] == 1:
            heapq.heappush(stone_type, -stone)
        if max_stone_in_group < stone:
            max_stone_in_group = stone
    answer = max_stone_in_group
    for start_index in range(1, len(stones) - k + 1):
        end_index = start_index + k - 1
        stone_group[stones[start_index - 1]] -= 1
        while len(stone_type) > 0 and stone_group[-stone_type[0]] == 0:
            heapq.heappop(stone_type)
        stone_group[stones[end_index]] += 1
        if stone_group[stones[end_index]] == 1:
            heapq.heappush(stone_type, -stones[end_index])
        max_stone_in_group = -stone_type[0]
        answer = min(answer, max_stone_in_group)
    return answer


print(solution([2, 2, 2, 1, 1], 1))

# def get_next_room(number):
#     if number not in next_rooms:
#         return number
#     next_number = next_rooms[number]
#     while next_number not in next_rooms:
#         next_rooms[number] = next_rooms[next_number]
#         number = next_number
#         next_number = next_rooms[number]
#     return next_number
