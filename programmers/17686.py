def string_to_file(file_name, index):
    buffer = ""
    head = ""
    number = -1
    tail = ""
    mode = 0
    for char in file_name:
        if mode == 0:
            if char.isdigit():
                head = buffer
                buffer = char
                mode = 1
            else:
                buffer += char
        elif mode == 1:
            if char.isdigit():
                buffer += char
            else:
                number = int(buffer)
                buffer = char
                mode = 2
        else:
            buffer += char
    if mode == 1:
        number = int(buffer)
    else:
        tail = buffer
    return head.lower(), number, index, tail.lower(), file_name


def solution(files):
    converted_files = []
    for i, file in enumerate(files):
        converted_files.append(string_to_file(file, i))
    converted_files.sort()
    return list(map(lambda file: file[4], converted_files))
