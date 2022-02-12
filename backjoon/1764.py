from sys import stdin

n, m = map(int, stdin.readline().split())
listen = sorted([stdin.readline().strip() for _ in range(n)])
see = sorted([stdin.readline().strip() for _ in range(m)])

result = []
i = 0
j = 0
while i < len(listen) and j < len(see):
    if listen[i] == see[j]:
        result.append(listen[i])
        i += 1
        j += 1
    elif listen[i] > see[j]:
        j += 1
    else:
        i += 1

print(len(result))
print("\n".join(result))
