def solution(info, edges):
    tree = [[] for _ in range(len(info))]

    for edge in edges:
        parent, child = edge[0], edge[1]
        tree[parent].append(child)

    result = 0
    sheep = 0
    wolf = 0

    def search_all_routes(possible_nodes: set):
        nonlocal sheep, wolf, result
        for node in possible_nodes:
            if info[node] == 0:
                sheep += 1
                if result < sheep:
                    result = sheep
                search_all_routes(possible_nodes.difference({node}).union(tree[node]))
                sheep -= 1
            else:
                if sheep > wolf + 1:
                    wolf += 1
                    search_all_routes(possible_nodes.difference({node}).union(tree[node]))
                    wolf -= 1

    search_all_routes({0})
    return result
