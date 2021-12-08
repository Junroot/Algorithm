knight_movements = [(2, -1), (2, 1), (-2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
max_board_point = 7

point_name = input()
point = (ord(point_name[0]) - ord("a"), int(point_name[1]) - 1)

result = 0
for movement in knight_movements:
    next_x, next_y = point[0] + movement[0], point[1] + movement[1]
    if 0 <= next_x <= max_board_point and 0 <= next_y <= max_board_point:
        result += 1

print(result)
