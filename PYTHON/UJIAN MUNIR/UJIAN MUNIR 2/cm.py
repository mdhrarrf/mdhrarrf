# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Mengkonversi Jarak

while True:
    KM_CM = 1000
    M_CM = 100

    cm1 = int(input('\nMasukan jarak (cm): '))

    km1 = int(cm1/KM_CM)
    km = cm1%KM_CM

    m1 = int(km/M_CM)
    m = km%M_CM

    print(f'\n{km1} km, {m1} m, {m} cm.')