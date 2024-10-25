# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Mengkonversi Uang

while True:
    uang1 = int(input('\nMasukan jumlah uang kelipatan 25: Rp. '))
    NILAI_PECAHAN1 = 1000
    NILAI_PECAHAN2 = 500
    NILAI_PECAHAN3 = 100
    NILAI_PECAHAN3 = 50
    NILAI_PECAHAN4 = 25

    seribu = int(uang1/NILAI_PECAHAN1)
    uang_hasil1 = uang1%NILAI_PECAHAN1

    lima_ratus = int(uang_hasil1/NILAI_PECAHAN2)
    uang_hasil2 = uang_hasil1%NILAI_PECAHAN2

    seratus = int(uang_hasil2/NILAI_PECAHAN3)
    uang_hasil3 = uang_hasil2%NILAI_PECAHAN3

    lima_puluh = int(uang_hasil3/NILAI_PECAHAN4)
    uang_hasil4= uang_hasil3%NILAI_PECAHAN3

    dua_lima = int(uang_hasil4/NILAI_PECAHAN4)

    print(f'\nUang senilai {uang1} setara dengan {seribu} buah Rp.{NILAI_PECAHAN1} {lima_ratus} buah Rp.{NILAI_PECAHAN2} {seratus} buah Rp.{NILAI_PECAHAN3} {lima_puluh} buah Rp.{NILAI_PECAHAN4} {dua_lima} buah Rp.{NILAI_PECAHAN4}')