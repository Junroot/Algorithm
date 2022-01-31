import sys

n = int(sys.stdin.readline())
strings = list(set([sys.stdin.readline().strip() for _ in range(n)]))

strings.sort(key=lambda x : (len(x), x))

print('\n'.join(set(strings)))
