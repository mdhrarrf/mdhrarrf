# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping For 7

total_sum = 0
expression = ""

for number in range(1, 6, 2):  # Menggunakan langkah 2 untuk angka ganjil
    if number > 1:
        expression += " + "
    expression += str(number)
    total_sum += number

expression += " = " + str(total_sum)

print(expression)
