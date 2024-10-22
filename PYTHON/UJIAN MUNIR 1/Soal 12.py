# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Ujian Munir Soal 12

while True:
    x = input('\nMasukan Angka Bulat 1: ')
    y = input('Masukan Angka Bulat 2: ')
    z = input('Masukan Angka Bulat 3: ')

    if x >= y and x >= z:
        print(f'\nAngka terbesarnya: {x}')
    elif y >= x and y >= z:
        print(f'\nAngka terbesarnya: {y}')
    elif z >= y and z >= x:
        print(f'\nAngka terbesarnya: {z}')

    if x <= y and x <= z:
        print(f'Angka terkecilnya: {x}')
    elif y <= x and y <= z:
        print(f'Angka terkecilnya: {y}')
    elif z <= y and z <= x:
        print(f'Angka terkecilnya: {z}')