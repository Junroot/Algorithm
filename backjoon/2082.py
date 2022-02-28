numbers = [
    ["###", "#.#", "#.#", "#.#", "###"],
    ["..#", "..#", "..#", "..#", "..#"],
    ["###", "..#", "###", "#..", "###"],
    ["###", "..#", "###", "..#", "###"],
    ["#.#", "#.#", "###", "..#", "..#"],
    ["###", "#..", "###", "..#", "###"],
    ["###", "#..", "###", "#.#", "###"],
    ["###", "..#", "..#", "..#", "..#"],
    ["###", "#.#", "###", "#.#", "###"],
    ["###", "#.#", "###", "..#", "###"],
]

clock = [[] for _ in range(4)]
cache = [[None for _ in range(9)] for _ in range(4)]


def validate(clock_index, number_index):
    if cache[clock_index][number_index] is not None:
        return cache[clock_index][number_index]
    number = numbers[number_index]
    for i in range(5):
        for j in range(3):
            if clock[clock_index][i][j] == "#" and number[i][j] == ".":
                cache[clock_index][number_index] = False
                return False
    cache[clock_index][number_index] = True
    return True


for _ in range(5):
    row_of_clock = input().split()
    for i in range(len(row_of_clock)):
        clock[i].append(row_of_clock[i])

result = ""
hour = 0
minute = 0

while hour < 24:
    first = hour // 10
    second = hour % 10
    if validate(0, first) and validate(1, second):
        result = str(first) + str(second) + ":"
        break
    hour += 1

while minute < 60:
    third = minute // 10
    fourth = minute % 10
    if validate(2, third) and validate(3, fourth):
        result += str(third) + str(fourth)
        break
    minute += 1

print(result)
