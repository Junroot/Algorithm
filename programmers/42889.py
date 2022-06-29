def solution(N, stages):
    stage_counts = [0 for _ in range(N + 2)]
    for stage in stages:
        stage_counts[stage] += 1
    passed_stage_counts = [0 for _ in range(N + 2)]
    passed_stage_counts[N + 1] = stage_counts[N + 1]
    for i in range(N, 0, -1):
        passed_stage_counts[i] = stage_counts[i] + passed_stage_counts[i + 1]
    result = []
    for i in range(1, N + 1):
        if stage_counts[i] == 0:
            result.append((0, i))
        else:
            result.append((-stage_counts[i] / passed_stage_counts[i], i))
    result.sort()
    return list(map(lambda x: x[1], result))
