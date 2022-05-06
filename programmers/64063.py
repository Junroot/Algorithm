import sys

sys.setrecursionlimit(10**8)


def solution(k, room_number):
    answer = []
    next_rooms = dict()

    def get_next_room(number):
        if number not in next_rooms:
            return number
        next_rooms[number] = get_next_room(next_rooms[number])
        return next_rooms[number]

    for room in room_number:
        next_room = get_next_room(room)
        answer.append(next_room)
        next_rooms[next_room] = next_room + 1

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
