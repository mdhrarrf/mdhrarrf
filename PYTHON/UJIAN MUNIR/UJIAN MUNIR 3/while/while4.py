# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping While 4

total_sum = 0
number = 1
expression = ""

while number <= 5:
    if number > 1:
        expression += " "
    expression += str(number)
    total_sum += number
    number += 1

expression += " = " + str(total_sum)

print(expression)