def solution(n, results):
    INF = int(1e9)
    win_graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    lose_graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        win_graph[i][i] = 0
        lose_graph[i][i] = 0
    for result in results:
        win_graph[result[0]][result[1]] = 1
        lose_graph[result[1]][result[0]] = 1

    for mid in range(1, n + 1):
        for source in range(1, n + 1):
            for destination in range(1, n + 1):
                win_graph[source][destination] = min(win_graph[source][destination],
                                                     win_graph[source][mid] + win_graph[mid][destination])
                lose_graph[source][destination] = min(lose_graph[source][destination],
                                                      lose_graph[source][mid] + lose_graph[mid][destination])

    count = 0
    for i in range(1, n + 1):
        win_count = len(list(filter(lambda x: x < INF, win_graph[i]))) - 1
        lose_count = len(list(filter(lambda x: x < INF, lose_graph[i]))) - 1
        if win_count + lose_count == n - 1:
            count += 1
    return count

