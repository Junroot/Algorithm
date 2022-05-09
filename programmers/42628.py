import heapq
from collections import defaultdict


def solution(operations):
    max_pq = []
    min_pq = []
    number_counts = defaultdict(int)
    for operation in operations:
        operator, operand = operation.split()
        operand = int(operand)
        if operator == "I":
            heapq.heappush(max_pq, -operand)
            heapq.heappush(min_pq, operand)
            number_counts[operand] += 1
        else:
            if len(max_pq) == 0:
                continue
            if operand == 1:
                max_number = -heapq.heappop(max_pq)
                number_counts[max_number] -= 1
            else:
                min_number = heapq.heappop(min_pq)
                number_counts[min_number] -= 1

        while len(max_pq) > 0 and number_counts[-max_pq[0]] == 0:
            heapq.heappop(max_pq)
        while len(min_pq) > 0 and number_counts[min_pq[0]] == 0:
            heapq.heappop(min_pq)

    if len(max_pq) == 0:
        return [0, 0]
    return [-max_pq[0], min_pq[0]]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
