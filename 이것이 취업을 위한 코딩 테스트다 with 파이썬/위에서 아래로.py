n = int(input())
numbers = [input() for _ in range(n)]

numbers.sort(reverse=True)

for number in numbers:
    print(number, end=" ")
