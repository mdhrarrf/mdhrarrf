# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Perpindahan Kalor Jenis Es

while True:
    print('\n\033[92m======================================')
    print('\033[31m     PROGRAM KALOR JENIS ES     ')
    print('\033[92m======================================')

    m = input('\033[33mMasukan Massa Benda (Kg): ')
    c = input('\033[37mMasukan Kalor Jenis Es (J/Kg): ')
    t = input('\033[0,35mMasukan Perubahan Suhu (C): ')

    hasil = int(m)*int(c)*int(t)
    print(f'\n\033[0,31mHasilnya adalah: {round (hasil,2)} J')