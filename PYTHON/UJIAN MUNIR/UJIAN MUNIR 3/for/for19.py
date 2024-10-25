# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping For 19

count = int(input('Masukan Berapa Banyak: '))
total = 0

for i in range(count):
    num = int(input(f'Masukan Angka {i+1}: '))
    total += num

average = total / count
print(f'\nJumlah: {total}')
print(f'Rata-Rata: {average}')