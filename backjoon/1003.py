from sys import stdin

t = int(stdin.readline())
numbers = [int(stdin.readline()) for _ in range(t)]
results = [(1, 0), (0, 1)]

for number in range(2, max(numbers) + 1):
    results.append((results[number - 2][0] + results[number - 1][0], results[number - 2][1] + results[number - 1][1]))

for number in numbers:
    result = results[number]
    print(str(result[0]) + " " + str(result[1]))
