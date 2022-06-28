def solution(n, weak, dist):
    dist.sort(reverse=True)
    MAX_INT = 987654321

    def get_min_count(weak_start, weak_end, used_bit):
        if weak_start == weak_end:
            return 0
        result = MAX_INT

        for dist_index in range(len(dist)):
            if (used_bit >> dist_index) % 2 == 1:
                continue
            move_distance = 0
            current = weak_start
            while move_distance <= dist[dist_index] and current != weak_end:
                move_distance = (move_distance + weak[(current + 1) % len(weak)] - weak[current] + n) % n
                current = (current + 1) % len(weak)
            result = min(result, 1 + get_min_count(current, weak_end, used_bit | (1 << dist_index)))
        return result

    result = MAX_INT
    for weak_start in range(len(weak)):
        current = (weak_start + 1) % len(weak)
        move_distance = (n + weak[current] - weak[weak_start]) % n
        while move_distance <= dist[0] and current != weak_start:
            move_distance = (move_distance + weak[(current + 1) % len(weak)] - weak[current] + n) % n
            current = (current + 1) % len(weak)
        result = min(result, 1 + get_min_count(current, weak_start, 1))

    if result >= MAX_INT:
        return -1
    return result
