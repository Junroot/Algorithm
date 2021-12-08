import random

lotto_numbers = list(range(1, 46))
lotto_count = 6
choices = []

for _ in range(lotto_count):
    lotto_number = random.choice(lotto_numbers)
    lotto_numbers.remove(lotto_number)
    choices.append(lotto_number)

print(choices)
