import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    operator = command[0]
    if operator == "push":
        stack.append(command[1])
    elif operator == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
            stack.pop()
    elif operator == "size":
        print(len(stack))
    elif operator == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    else:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])

