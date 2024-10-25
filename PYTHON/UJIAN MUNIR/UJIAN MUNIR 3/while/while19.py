# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping While 19

count = int(input('Masukan Berapa Banyak: '))
total = 0
i = 0

while i < count:
    num = int(input(f'Masukan Angka {i + 1}: '))
    total += num
    i += 1

average = total / count
print(f'\nJumlah: {total}')
print(f'Rata-Rata: {average}')
