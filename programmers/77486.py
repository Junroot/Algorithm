from collections import deque


class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.parent = None


def solution(enroll, referral, seller, amount):
    members_by_name = dict()
    members_by_id = []
    left_child_count = [0 for _ in range(len(enroll) + 1)]
    for id, name in enumerate(enroll):
        member = Member(id, name)
        members_by_name[name] = member
        members_by_id.append(member)
    root = Member(len(enroll), "-")
    members_by_name["-"] = root
    members_by_id.append(root)

    for child_id, parent_name in enumerate(referral):
        parent = members_by_name[parent_name]
        members_by_id[child_id].parent = parent
        left_child_count[parent.id] += 1

    margins = [[] for _ in range(len(enroll) + 1)]

    for amount_index, s in enumerate(seller):
        margins[members_by_name[s].id].append(amount[amount_index] * 100)

    queue = deque()

    for i in range(len(enroll) + 1):
        if left_child_count[i] == 0:
            queue.append(i)

    while queue:
        member = members_by_id[queue.popleft()]
        if member.parent is None:
            continue
        parent_id = member.parent.id
        left_child_count[parent_id] -= 1
        if left_child_count[parent_id] == 0:
            queue.append(parent_id)
        for i, margin in enumerate(margins[member.id]):
            commission = margin // 10
            if commission > 0:
                margins[parent_id].append(commission)
                margins[member.id][i] -= commission

    return list(map(sum, margins[:-1]))
