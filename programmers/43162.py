from collections import deque


def bfs(computer, visited, computers):
    queue = deque([computer])
    while queue:
        current_computer = queue.popleft()
        visited[current_computer] = True
        connections = computers[current_computer]
        for i, connection in enumerate(connections):
            if not visited[i] and connection:
                queue.append(i)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for i, computer in enumerate(visited):
        if not computer:
            answer += 1
            bfs(i, visited, computers)

    return answer
