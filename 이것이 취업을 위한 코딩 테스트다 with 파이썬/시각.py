n = int(input())
count = 0
number_to_find = str(3)


for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if number_to_find in str(h) + str(m) + str(s):
                count += 1


print(count)
