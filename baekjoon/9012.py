import sys

stdin = sys.stdin
n = int(stdin.readline())

for _ in range(n):
    string = stdin.readline().rstrip()
    depth = 0
    success = True
    for char in string:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth < 0:
                success = False
                break
    if success and depth == 0:
        print("YES")
    else:
        print("NO")
