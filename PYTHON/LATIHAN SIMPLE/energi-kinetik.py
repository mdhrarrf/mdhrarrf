# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Energi Kinetik

while True:
    print('\n\033[92m=====================================')
    print('\033[31m        PROGRAM ENERGI KINETIK       ')
    print('\033[92m=====================================')

    m = input('\033[33mMasukan Massa Benda (Kg): ')
    v2 = int(input('\033[33mMasukan Kecepatan Benda (Km/H): '))*int(2)
    ek = int(1)/int(2)*int(m)*int(v2)

    print(f'\n\033[37mJawabannya adalah: {round (ek,2)} J')