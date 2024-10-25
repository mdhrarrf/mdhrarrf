# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Logika Menukar Nilai Bilangan

while True:
    x = input('\nMasukan bilangan bulat X\t: ')
    y = input('Masukan bilangan bulat Y\t: ')
    z = input('Masukan bilangan bulat Z\t: ')

    temp = x
    x = y
    y = z
    z = temp

    print(f'\nBilangan Y = {x}')
    print(f'Bilangan Z = {y}')
    print(f'Bilangan X = {z}')