n, m = map(int, input().split())
leaders = [i for i in range(n + 1)]


def find_group_number(student):
    leader = leaders[student]
    while leaders[leader] != leader:
        leader = leaders[leader]
    leaders[student] = leader
    return leader


def merge(student1, student2):
    group1 = find_group_number(student1)
    group2 = find_group_number(student2)
    if group1 < group2:
        leaders[group2] = group1
    elif group2 < group1:
        leaders[group1] = group2


def is_same_team(student1, student2):
    return find_group_number(student1) == find_group_number(student2)


for _ in range(m):
    op, student1, student2 = map(int, input().split())
    if op == 0:
        merge(student1, student2)
    if op == 1:
        if is_same_team(student1, student2):
            print("YES")
        else:
            print("NO")
