t = int(input())

for _ in range(t):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(scores[0][0], scores[1][0]))
        continue

    cache = [[scores[0][0], scores[1][0] + scores[0][1]], [scores[1][0], scores[0][0] + scores[1][1]]]

    for i in range(2, n):
        cache[0].append(max(cache[1][i - 1], cache[1][i - 2]) + scores[0][i])
        cache[1].append(max(cache[0][i - 1], cache[0][i - 2]) + scores[1][i])

    print(max(cache[0][n - 1], cache[1][n - 1]))
