def solution(routes):
    routes.sort(key=lambda x: (x[1], -x[0]))
    camera = routes[0][1]
    answer = 1
    for i in range(1, len(routes)):
        route = routes[i]
        if route[0] <= camera <= route[1]:
            continue
        if camera <= route[0]:
            camera = route[1]
            answer += 1
    return answer
