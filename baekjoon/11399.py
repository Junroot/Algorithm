n = int(input())
p_list = sorted(list(map(int, input().split())))

result = 0
for i in range(n):
    result += p_list[i] * (n - i)

print(result)
