import sys

t = int(sys.stdin.readline())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().strip().split())
    x = (n - 1) // h + 1
    y = (n - 1) % h + 1
    print(y * 100 + x)

