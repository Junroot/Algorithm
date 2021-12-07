result = 0
num = 1

while num <= 1000:
    if (num % 3) == 0:
        result += num
    num += 1

print(result)