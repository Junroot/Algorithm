pibo = [0, 1]
next_index = 2

n = int(input())

if n >= 0:
    print(0)

while pibo[next_index - 1] <= n:
    print(pibo[next_index - 1])
    pibo.append(pibo[next_index - 1] + pibo[next_index - 2])
    next_index += 1
