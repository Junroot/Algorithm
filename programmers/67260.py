from collections import deque


def solution(n, path, order):
    graph = [[] for _ in range(n)]

    for rooms in path:
        graph[rooms[0]].append(rooms[1])
        graph[rooms[1]].append(rooms[0])

    locked_rooms = dict()

    for rooms in order:
        if rooms[1] == 0:
            return False
        locked_rooms[rooms[1]] = rooms[0]

    visited = [False for _ in range(n)]
    visited[0] = True

    waited_rooms = dict()
    queue = deque([0])

    while queue:
        room = queue.popleft()
        for next_room in graph[room]:
            if visited[next_room]:
                continue

            if next_room in locked_rooms:
                if visited[locked_rooms[next_room]]:
                    visited[next_room] = True
                    queue.append(next_room)
                else:
                    waited_rooms[locked_rooms[next_room]] = next_room
            else:
                visited[next_room] = True
                queue.append(next_room)
                if next_room in waited_rooms:
                    unlocked_room = waited_rooms[next_room]
                    visited[unlocked_room] = True
                    queue.append(unlocked_room)

    return sum(visited) == n

print(solution(2, [[0, 1]], [[0, 1]]))
