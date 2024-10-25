# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Jarak Lensa

while True:
    print('\n\033[92m========================================')
    print('\033[31m PROGRAM JARAK LENSA OBJEKTIF & OKULER  ')
    print('\033[92m========================================')

    fob = input('\033[33mMasukan Jarak Lensa Objektif (cm): ')
    fok = input(' \033[33mMasukan Jarak Lensa Okuler (cm): ')

    d = int(fob)+int(4)+int(fok)

    print(f'\n\033[37mJawabannya Adalah: {round (d,2)} cm')