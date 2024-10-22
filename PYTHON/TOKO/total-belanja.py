# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Toko (Total Belanja)

while True:
    print('\n\033[92m==============================')
    print('\033[31m PROGRAM DISKON TOTAL BELANJA ')
    print('\033[92m==============================')

    total = int(input('\033[33mMasukan total belanja anda: Rp. '))

    if total >= int(100000):
        print('\n\033[37mAnda Mendapatkan Diskon!')

    elif total <= int(100000):
        print('\n\033[37mAnda Tidak Mendapatkan Diskon!')
