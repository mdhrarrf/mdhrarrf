# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Mengurutkan No dari Terkecil ke Terbesar

while True:
    angka1 = input('\nMasukan bilangan bilangan 1: ')
    angka2 = input('Masukan bilangan bilangan 2: ')
    angka3 = input('Masukan bilangan bilangan 3: ')

    if angka1 >= angka2 and angka2 >= angka3:
        print(f'\n{angka1}, {angka2}, {angka3}')
    elif angka2 >= angka1 and angka1 >= angka3:
        print(f'\n{angka2}, {angka1}, {angka3}')
    elif angka3 >= angka2 and angka2 >= angka1:
        print(f'\n{angka3}, {angka2}, {angka1}')
    elif angka1 <= angka2 and angka2 <= angka3:
        print(f'\n{angka2}, {angka3}, {angka1}')
    elif angka2 <= angka1 and angka1 <= angka3:
        print(f'\n{angka3}, {angka1}, {angka2}')
    elif angka3 <= angka2 and angka2 <= angka1:
        print(f'\n{angka1}, {angka2}, {angka3}')