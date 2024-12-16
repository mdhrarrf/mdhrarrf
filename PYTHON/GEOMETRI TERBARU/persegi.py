# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Persegi

PHI = 3.14

def hitung_persegi(sisi):
    luas = round(sisi ** 2)
    keliling = round(4 * sisi)
    return luas, keliling

print("\033[1;34mProgram Geometri: Menghitung Luas dan Keliling Persegi\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi = float(input("Masukkan sisi persegi: "))
    luas_persegi, keliling_persegi = hitung_persegi(sisi)
    print("\nPersegi:")
    print(f"Luas:\t\t{luas_persegi}")
    print(f"Keliling:\t{keliling_persegi}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_persegi()
