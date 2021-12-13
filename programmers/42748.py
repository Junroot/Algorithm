def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        inner_array = array[i - 1: j]
        inner_array.sort()
        answer.append(inner_array[k - 1])
    return answer
