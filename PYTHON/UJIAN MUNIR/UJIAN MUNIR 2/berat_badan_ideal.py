# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Berat Badan Ideal

while True:
    tb = int(input('\nMasukan tinggi badan mu (cm)\t: '))

    HASIL_BAGI = tb-int(100)
    DISKON = int(10)/int(100)*HASIL_BAGI
    PENGURANGAN = HASIL_BAGI-DISKON
    
    print(f'Ideal bb mu {PENGURANGAN} kg')
