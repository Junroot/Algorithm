from sys import stdin

n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
sorted_nums = sorted(set(numbers))
compressed_nums = dict()

for i in range(len(sorted_nums)):
    compressed_nums[sorted_nums[i]] = i

result = [str(compressed_nums[number]) for number in numbers]

print(" ".join(result))
