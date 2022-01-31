import sys

t = int(sys.stdin.readline())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().strip().split())
    x = (n - 1) // h + 1
    y = (n - 1) % h + 1
    print(y, end="")
    if x < 10:
        print("0" + str(x))
    else:
        print(x)
