string1 = input()
string2 = input()

cache = [[0 for _ in range(len(string1) + 1)] for _ in range(len(string2) + 1)]

for i in range(1, len(string2) + 1):
    for j in range(1, len(string1) + 1):
        if string1[j - 1] == string2[i - 1]:
            cache[i][j] = cache[i - 1][j - 1] + 1
            continue
        cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

max_length = cache[-1][-1]
result = ""
left_length = max_length
cache_position = [len(string1), len(string2)]

while left_length > 0:
    x = cache_position[0]
    y = cache_position[1]
    if x > 1 and cache[y][x] == cache[y][x-1]:
        cache_position[0] -= 1
    elif y > 1 and cache[y][x] == cache[y - 1][x]:
        cache_position[1] -= 1
    else:
        result = string1[cache_position[0] - 1] + result
        cache_position[0] -= 1
        cache_position[1] -= 1
        left_length -= 1


print(max_length)
if max_length != 0:
    print(result)
