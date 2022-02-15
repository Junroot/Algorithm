from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
names = {}
numbers = {}

for i in range(1, n + 1):
    name = stdin.readline().rstrip()
    str_i = str(i)
    names[str_i] = name
    numbers[name] = str_i

problems = [stdin.readline().rstrip() for _ in range(m)]


def is_number(char):
    return '0' <= char <= '9'


result = []

for problem in problems:
    if is_number(problem[0]):
        result.append(names[problem])
    else:
        result.append(numbers[problem])

stdout.write("\n".join(result))
