from sys import stdin

v, e = map(int, stdin.readline().split())
edges = []
parents = [i for i in range(v + 1)]

for _ in range(e):
    start, end, weight = map(int, stdin.readline().split())
    edges.append((weight, start, end))

edges.sort()


def get_team_number(vertex):
    while parents[vertex] != vertex:
        vertex = parents[vertex]
    return vertex


def is_same_group(vertex1, vertex2):
    return get_team_number(vertex1) == get_team_number(vertex2)


def merge(vertex1, vertex2):
    team1 = get_team_number(vertex1)
    team2 = get_team_number(vertex2)
    if team1 < team2:
        parents[team2] = team1
    else:
        parents[team1] = team2


result = 0
count = 0
for weight, start, end in edges:
    if is_same_group(start, end):
        continue

    merge(start, end)
    result += weight
    count += 1
    if count == v - 1:
        break


print(result)
