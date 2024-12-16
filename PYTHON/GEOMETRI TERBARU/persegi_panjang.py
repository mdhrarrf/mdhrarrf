# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Persegi Panjang

PHI = 3.14

def hitung_persegi_panjang(panjang, lebar):
    luas = round(panjang * lebar)
    keliling = round(2 * (panjang + lebar))
    return luas, keliling

print("\033[1;34mProgram Geometri: Menghitung Luas dan Keliling Persegi Panjang\033[0m")
print("-------------------------------------------------------------")
while True:
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas_persegi_panjang, keliling_persegi_panjang = hitung_persegi_panjang(panjang, lebar)
    print("\nPersegi Panjang:")
    print(f"Luas:\t\t{luas_persegi_panjang}")
    print(f"Keliling:\t{keliling_persegi_panjang}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_persegi_panjang()