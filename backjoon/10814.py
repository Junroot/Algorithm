import sys

n = int(sys.stdin.readline())
members = []

for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    members.append((int(age), i, name))

members.sort()

for member in members:
    print(str(member[0]) + ' ' + member[2])
