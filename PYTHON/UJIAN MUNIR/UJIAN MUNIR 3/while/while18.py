# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping While 18

n = int(input('Masukan Berapa Banyak: '))

i = 1
while i <= n:
    j = 1
    while j <= n:
        print(f'{i} x {j} = {i * j}', end='\t')
        j += 1
    print()
    i += 1
