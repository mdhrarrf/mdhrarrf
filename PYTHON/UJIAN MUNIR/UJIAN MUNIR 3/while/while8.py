# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping While 8

total_sum = 0
number = 2
expression = ""

while number <= 10:
    if number > 2:
        expression += " + "
    expression += str(number)
    total_sum += number
    number += 2

expression += " = " + str(total_sum)

print(expression)