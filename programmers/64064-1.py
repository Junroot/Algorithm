def is_matched(user, banned):
    if len(user) != len(banned):
        return False
    for i in range(len(user)):
        if user[i] != banned[i] and banned[i] != '*':
            return False
    return True


def count_combination(matched_ids, used_ids, current_index):
    result = set()
    if current_index == len(matched_ids):
        used_bit = 0
        for used_id in used_ids:
            used_bit = used_bit | 1 << used_id
        return {used_bit}
    for matched_id in matched_ids[current_index]:
        if matched_id in used_ids:
            continue
        used_ids.add(matched_id)
        result = result.union(count_combination(matched_ids, used_ids, current_index + 1))
        used_ids.remove(matched_id)
    return result


def solution(user_id, banned_id):
    matched_ids = [[] for _ in range(len(banned_id))]
    for i, banned in enumerate(banned_id):
        for j, user in enumerate(user_id):
            if is_matched(user, banned):
                matched_ids[i].append(j)
    return len(count_combination(matched_ids, set(), 0))

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
