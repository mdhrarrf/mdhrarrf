# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Menghitung Jarak dari Tanggal

while True:
    TAHUN_HARI = 365
    BULAN_HARI = 30

    hari1 = int(input('\nMasukan Tanggal 1\t: '))
    hari2 = int(input('Masukan Tanggal 2\t: '))

    tahun1 = int(hari1/TAHUN_HARI)
    hari1 = hari1%TAHUN_HARI
    bulan1 = int(hari1/BULAN_HARI)
    hari1 = hari1%BULAN_HARI

    tahun2 = int(hari2/TAHUN_HARI)
    hari2 = hari2%TAHUN_HARI
    bulan2 = int(hari2/BULAN_HARI)
    hari2 = hari2%BULAN_HARI

    print(f'\n(1) {tahun1} Tahun, {bulan1} Bulan, {hari1} Hari')
    print(f'(2) {tahun2} Tahun, {bulan2} Bulan, {hari2} Hari')

    if hari1 >= hari2:
        print(f'\n{tahun1-tahun2} Tahun, {bulan1-bulan2} Bulan, {hari1-hari2} Hari')
    elif hari1 <= hari2:
        print(f'\n{tahun2-tahun1} Tahun, {bulan2-bulan1} Bulan, {hari2-hari1} Hari')