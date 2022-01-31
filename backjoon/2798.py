import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
sums = []

for i in range(0, len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            sums.append(cards[i] + cards[j] + cards[k])

sums.sort(reverse=True)

for sum in sums:
    if sum <= m:
        print(sum)
        break
