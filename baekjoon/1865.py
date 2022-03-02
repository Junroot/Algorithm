from sys import stdin

INF = 1e8
input = stdin.readline

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = dict()

    def update_edge(s, e, t):
        if (s, e) in edges:
            edges[(s, e)] = min(edges[(s, e)], t)
        else:
            edges[(s, e)] = t


    def check():
        distances = [INF for _ in range(n + 1)]
        for i in range(n):
            for current, next in edges:
                weight = edges[(current, next)]
                if distances[next] > distances[current] + weight:
                    distances[next] = distances[current] + weight
                    if i == n - 1:
                        return True
        return False


    for _ in range(m):
        s, e, t = map(int, input().split())
        update_edge(s, e, t)
        update_edge(e, s, t)

    for _ in range(w):
        s, e, t = map(int, input().split())
        update_edge(s, e, -t)

    if check():
        print("YES")
    else:
        print("NO")

