# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Toko (Diskon 12,5%)

while True:
    print('\n\033[92m=======================================')
    print('\033[31m      PROGRAM DISKON BARANG 12,5%      ')
    print('\033[92m=======================================')

    harga = (input('\033[33mMasukan harga barang anda: Rp. '))
    diskon = float(12.5)/int(100)
    hasil = int(harga)*diskon
    hasil2 = int(harga)-int(hasil)

    print(f'\n\033[37mHarga barang setelah diberikan diskon: Rp. {hasil2}')