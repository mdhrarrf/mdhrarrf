# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Kalor Jenis Air

while True:
    print('\n\033[92m==================================')
    print('\033[31m     PROGRAM KALOR JENIS AIR')
    print('\033[92m==================================')

    m = input('\033[33mMasukan Massa Benda (Kg): ')
    c = input('\033[33mMasukan Kalor Jenis Air (J/Kg): ')
    t = input('\033[33mMasukan Perubahan Suhu Air (C): ')

    hasil = int(m)*int(c)*int(t)

    print(f'\n\033[37mHasilnya Adalah: {round (hasil,2)} J')