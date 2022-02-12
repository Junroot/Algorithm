from sys import stdin

n = int(stdin.readline())
paper = [stdin.readline().split() for _ in range(n)]
sub_papers = [lambda left_top, half_length: left_top,
             lambda left_top, half_length: (left_top[0] + half_length, left_top[1]),
             lambda left_top, half_length: (left_top[0], left_top[1] + half_length),
             lambda left_top, half_length: (left_top[0] + half_length, left_top[1] + half_length)]


def get_color(left_top, length):
    x, y = left_top
    color = paper[y][x]
    for i in range(y, y + length):
        for j in range(x, x + length):
            if paper[i][j] != color:
                return "-1"
    return color


def count_color(left_top, length):
    color = get_color(left_top, length)
    if color == "0":
        return 1, 0
    elif color == "1":
        return 0, 1
    half_length = length // 2
    result = (0, 0)

    for sub_paper in sub_papers:
        sub_result = count_color(sub_paper(left_top, half_length), half_length)
        result = (result[0] + sub_result[0], result[1] + sub_result[1])
    return result


result = count_color((0, 0), n)
print(result[0])
print(result[1])
