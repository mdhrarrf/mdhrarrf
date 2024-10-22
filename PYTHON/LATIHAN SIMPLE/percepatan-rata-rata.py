# Muhammad Haidar Almer Rafif
# 22/10/24
# Program Percepatan Rata-rata

while True:
    print('\n\033[92m================================')
    print('\33[31m  PROGRAM PERCEPATAN RATA-RATA  ')
    print('\033[92m================================')

    v1 = input('\033[33mMasukan Kecepatan Awal: ')
    v2 = input('\033[33mMasukan Kecepatan Akhir: ')

    t1 = input('\n\033[36mMasukan Waktu Awal: ')
    t2 = input('\033[36mMasukan Waktu Akhir: ')

    v1v2 = int(v1) - int(v2)
    t1t2 = int(t1) - int(t2)

    hasil = int(v1v2)/int(t1t2)
    
    print(f'\n\033[37mHasilnya adalah: {round (hasil,2)} m/s')