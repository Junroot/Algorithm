def dfs(tickets, now):
    if not tickets:
        return True, [now]
    for i, ticket in enumerate(tickets):
        if ticket[0] == now:
            tail = dfs(tickets[:i] + tickets[i + 1:], ticket[1])
            if tail[0]:
                return True, [now] + tail[1]
    return False, []


def solution(tickets):
    tickets.sort()
    return dfs(tickets, "ICN")[1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
