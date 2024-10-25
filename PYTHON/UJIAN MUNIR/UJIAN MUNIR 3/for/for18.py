# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping For 18

n = int(input('Masukan Berapa Banyak: '))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{i} x {j} = {i*j}',end='\t')
    print()