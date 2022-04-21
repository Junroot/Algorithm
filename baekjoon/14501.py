days = int(input())
consults = []

for day in range(1, days + 1):
    t, p = map(int, input().split())
    consults.append((day + t - 1, day, p))

consults.sort()

cache = [0]
consult_index = 0

for day in range(1, consults[-1][0] + 1):
    cache.append(cache[day - 1])
    while consult_index < len(consults) and consults[consult_index][0] == day:
        cache[day] = max(cache[day], consults[consult_index][2] + cache[consults[consult_index][1] - 1])
        consult_index += 1

print(cache[days])
