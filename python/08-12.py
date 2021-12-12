def DashInsert(string):
    result = string[0]
    is_odd = (int(string[0]) % 2 == 1)
    for i in range(1, len(string)):
        next_odd = (int(string[i]) % 2 == 1)
        if is_odd and next_odd:
            result += "-"
        elif not is_odd and not next_odd:
            result += "*"
        else:
            is_odd = next_odd
        result += string[i]
    return result


print(DashInsert("4546793"))
