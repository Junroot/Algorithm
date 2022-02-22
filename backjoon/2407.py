n, m = map(int, input().split())
factorials = [1]

for i in range(1, n + 1):
    factorials.append(factorials[i - 1] * i)

print(factorials[n] // factorials[m] // factorials[n - m])