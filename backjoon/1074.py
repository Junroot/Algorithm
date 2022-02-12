n, r, c = map(int, input().split())
search_list = [lambda left_top, half_length: left_top,
               lambda left_top, half_length: (left_top[0] + half_length, left_top[1]),
               lambda left_top, half_length: (left_top[0], left_top[1] + half_length),
               lambda left_top, half_length: (left_top[0] + half_length, left_top[1] + half_length)]


def is_in(left_top, length):
    x, y = left_top
    return x <= c < x + length and y <= r < y + length


def find_order(left_top, length):
    if length == 1:
        return 0
    half_length = length // 2
    result = 0
    for search in search_list:
        new_top_left = search(left_top, half_length)
        if is_in(new_top_left, half_length):
            return find_order(new_top_left, half_length) + result
        result += half_length ** 2


print(find_order((0, 0), 2 ** n))