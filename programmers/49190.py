def solution(arrows):
    answer = 0
    now = (0, 0)
    directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    edges = set()
    visited = {(0, 0)}
    for arrow in arrows:
        new = (now[0] + directions[arrow][0], now[1] + directions[arrow][1])
        new_edge = (now, new)
        if new_edge not in edges:
            if new in visited:
                answer += 1
            if (arrow == 1 or arrow == 3) and ((now[0] + 1, now[1]), (new[0] - 1, new[1])) in edges:
                answer += 1
            elif (arrow == 5 or arrow == 7) and ((now[0] - 1, now[1]), (new[0] + 1, new[1])) in edges:
                answer += 1
        visited.add(new)
        edges.add(new_edge)
        edges.add((new, now))
        now = new
    return answer

solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])
