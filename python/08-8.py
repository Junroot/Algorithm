with open("abc.txt", "r") as file:
    lines = file.readlines()
    lines.reverse()
    with open("abc.txt", "w") as file2:
        file2.writelines(lines)
