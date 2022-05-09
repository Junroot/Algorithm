from collections import defaultdict


def solution(id_list, report, k):
    user_ids_by_name = {name: id for id, name in enumerate(id_list)}
    reported_ids = defaultdict(set)

    for r in report:
        reporting_user, reported_user = r.split()
        reported_ids[user_ids_by_name[reported_user]].add(user_ids_by_name[reporting_user])

    result = [0 for _ in range(len(id_list))]

    for reported_id in reported_ids:
        if len(reported_ids[reported_id]) >= k:
            for reporting_id in reported_ids[reported_id]:
                result[reporting_id] += 1
    return result

