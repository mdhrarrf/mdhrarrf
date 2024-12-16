# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Lingkaran

PHI = 3.14

def hitung_lingkaran(jari_jari):
    luas = round(PHI * (jari_jari ** 2))
    keliling = round(2 * PHI * jari_jari)
    return luas, keliling

print("\033[1;34mProgram Geometri: Menghitung Luas dan Keliling Lingkaran\033[0m")
print("-------------------------------------------------------------")
while True:
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas_lingkaran, keliling_lingkaran = hitung_lingkaran(jari_jari)
    print("\nLingkaran:")
    print(f"Luas:\t\t{luas_lingkaran}")
    print(f"Keliling:\t{keliling_lingkaran}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_lingkaran()