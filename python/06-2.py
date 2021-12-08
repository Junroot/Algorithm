quotient_of_three = 1000 // 3
quotient_of_five = 1000 // 5
quotient_of_fifteen = 1000 // 15

sum_of_three = quotient_of_three * (quotient_of_three + 1) * 3 // 2
sum_of_five = quotient_of_five * (quotient_of_five + 1) * 5// 2
sum_of_fifteen = quotient_of_fifteen * (quotient_of_fifteen + 1) * 15 // 2

print(sum_of_three + sum_of_five - sum_of_fifteen)
