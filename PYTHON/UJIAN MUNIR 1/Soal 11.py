# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Ujian Munir Soal 11

while True:
    nilai = int(input('Masukan Nilai: '))

    if nilai >= 90 and nilai <= 100:
        print('A')
    elif nilai >= 80 and nilai <= 90:
        print('B')
    elif nilai >= 70 and nilai <= 80:
        print('C')
    elif nilai >= 60 and nilai <= 70:
        print('D')
    elif nilai <= 60:
        print('E')