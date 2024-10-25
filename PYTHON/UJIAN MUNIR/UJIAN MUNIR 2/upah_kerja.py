# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Menghitung Upah Perjam

while True:
    UPAH_JAM1 = 'Rp. 4000'
    UPAH_JAM2 = 'Rp. 5000'
    UPAH_JAM3 = 'Rp. 6000'
    UPAH_JAM4 = 'Rp. 7500'

    jam = input('\nMasukan berapa lama anda lembur (jam): ')

    if jam == '1':
        print(f'Upah perjam anda: {UPAH_JAM1}')
    elif jam == '2':
        print(f'Upah perjam anda: {UPAH_JAM2}')
    elif jam == '3':
        print(f'Upah perjam anda: {UPAH_JAM3}')
    elif jam == '4':
        print(f'Upah perjam anda: {UPAH_JAM4}')
    elif jam == '0':
        print('Anda tidak lembur')
    else:
        print('Anda terlalu rajin lembur')