# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping For 20

n = int(input('Masukan jumlah perkalian: '))

for i in range (1, n + 1):
    for j in range(1, n + 1):
        print(f'{i*j}'.rjust(4),end=' ')
    print()