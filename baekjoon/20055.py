belt_length, maximum_fault_space = map(int, input().split())
out_point = belt_length - 1
in_point = 0
belt_length *= 2
lifes = list(map(int, input().split()))
robots = [False for _ in range(belt_length)]
fault_space_count = 0

phase = 0


def rotate():
    global in_point, out_point
    in_point = (in_point - 1 + belt_length) % belt_length
    out_point = (out_point - 1 + belt_length) % belt_length
    robots[out_point] = False


def put_robot(index):
    global fault_space_count
    robots[index] = True
    lifes[index] -= 1
    if lifes[index] == 0:
        fault_space_count += 1
    if index == out_point:
        robots[index] = False


def move_robots():
    global fault_space_count
    index = (out_point - 1 + belt_length) % belt_length
    next_index = out_point
    while index != in_point:
        if robots[index] and not robots[next_index] and lifes[next_index] > 0:
            robots[index] = False
            put_robot(next_index)
        next_index = index
        index = (index - 1 + belt_length) % belt_length


def put_new_robot():
    if lifes[in_point] > 0:
        put_robot(in_point)


while fault_space_count < maximum_fault_space:
    phase += 1
    rotate()
    move_robots()
    put_new_robot()

print(phase)
