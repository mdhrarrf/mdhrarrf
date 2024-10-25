# Muhammad Haidar Almer Rafif
# 25/10/24
# Program Mengkonversi Angka ke Angka Romawi

while True:
    def konversi_romawi_1_10(n):
        peta_romawi = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X'
        }
        
        if n in peta_romawi:
            return peta_romawi[n]
        else:
            return "\nBilangan harus antara 1 dan 10"

    bilangan = int(input("\nMasukkan bilangan bulat positif (1-10): "))
    hasil = konversi_romawi_1_10(bilangan)

    print(f"\nAngka Romawi: {hasil}")