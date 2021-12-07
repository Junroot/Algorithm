from queue import PriorityQueue


def solution(n, costs):
    count = 0
    answer = 0
    parents_per_island = [i for i in range(n)]
    queue = PriorityQueue()
    for cost in costs:
        queue.put((cost[2], cost[0], cost[1]))
    while count != n - 1:
        cost = queue.get()
        first = cost[1]
        second = cost[2]

        if parents_per_island[first] == parents_per_island[second]:
            continue
        change_parent(parents_per_island, parents_per_island[second], parents_per_island[first])
        answer += cost[0]
        count += 1
    return answer


def change_parent(parents_per_island, from_parent, to_parent):
    for i in range(len(parents_per_island)):
        if parents_per_island[i] == from_parent:
            parents_per_island[i] = to_parent

