string = input()
now_char = string[0]
combo = 1
result = ""

for i, next_char in enumerate(string, 1):
    if now_char == next_char:
        combo += 1
    else:
        result += now_char + str(combo)
        now_char = next_char
        combo = 1

result += now_char + str(combo)

print(result)
