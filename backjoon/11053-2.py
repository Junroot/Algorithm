n = int(input())
numbers = list(map(int, input().split()))
dp = [1]

for i in range(1, len(numbers)):
    number = numbers[i]
    result = 1
    for j in range(i):
        if numbers[j] < number:
            result = max(result, dp[j] + 1)
    dp.append(result)

print(max(dp))
