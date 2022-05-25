import string

def remove_continuous_dots(new_id):
    temp = ""
    last_char = ""
    for char in new_id:
        if char == "." and last_char == ".":
            continue
        temp += char
        last_char = char
    return temp


def trim_dot(new_id):
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[: -1]
    return new_id


def solution(new_id):
    char_set = {'-', '_', '.'} | set(string.digits) | set(string.ascii_lowercase)
    new_id = new_id.lower()

    temp = ""
    for char in new_id:
        if char in char_set:
            temp += char
    new_id = temp
    new_id = remove_continuous_dots(new_id)
    new_id = trim_dot(new_id)

    if len(new_id) == 0:
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[:15]

    new_id = trim_dot(new_id)

    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id

print(solution("=.="))
