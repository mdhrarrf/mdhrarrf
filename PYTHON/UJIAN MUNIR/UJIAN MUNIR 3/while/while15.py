# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Looping While 15

tinggi = 5
baris = 1

while baris <= tinggi:
    spasi = tinggi - baris

    print(' ' * spasi, end='')
    print('*' * (2 * baris - 1))

    baris += 1