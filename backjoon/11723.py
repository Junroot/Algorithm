from sys import stdin
from sys import stdout

existence = [False for _ in range(21)]

m = int(stdin.readline())

for _ in range(m):
    command = stdin.readline().strip().split()
    if command[0] == "add":
        existence[int(command[1])] = True
    elif command[0] == "remove":
        existence[int(command[1])] = False
    elif command[0] == "check":
        if existence[int(command[1])]:
            stdout.write("1\n")
        else:
            stdout.write("0\n")
    elif command[0] == "toggle":
        number = int(command[1])
        existence[number] = not existence[number]
    elif command[0] == "all":
        for i in range(len(existence)):
            existence[i] = True
    else:
        for i in range(len(existence)):
            existence[i] = False
