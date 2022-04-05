import bisect

n = int(input())
numbers = list(map(int, input().split()))
sequence = [numbers[0]]
sequence_indexes = [0]

for i in range(1, n):
    number = numbers[i]
    index_to_insert = bisect.bisect_left(sequence, number)
    if index_to_insert == len(sequence):
        sequence.append(number)
    else:
        sequence[index_to_insert] = number
    sequence_indexes.append(index_to_insert)

result_sequence = []
now = len(sequence) - 1

for i in range(n - 1, -1, -1):
    if now == sequence_indexes[i]:
        result_sequence.append(numbers[i])
        now -= 1

print(len(sequence))
print(*(reversed(result_sequence)))
