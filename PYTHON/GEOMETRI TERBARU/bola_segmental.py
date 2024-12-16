# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Bola Segmental

PHI = 3.14

def hitung_bola_segmental(jari_jari, tinggi):
    volume = round((1/3) * PHI * (tinggi ** 2) * (3 * jari_jari - tinggi))
    luas_permukaan = round(PHI * (jari_jari ** 2) + PHI * (tinggi * (2 * jari_jari - tinggi)))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Bola Segmental\033[0m")
print("-------------------------------------------------------------")
while True:
    jari_jari_bola_segmental = float(input("Masukkan jari-jari bola segmental: "))
    tinggi_bola_segmental = float(input("Masukkan tinggi bola segmental: "))
    volume_bola_segmental, luas_permukaan_bola_segmental = hitung_bola_segmental(jari_jari_bola_segmental, tinggi_bola_segmental)
    print("\nBola Segmental:")
    print(f"Volume:\t\t{volume_bola_segmental}")
    print(f"Luas Permukaan:\t{luas_permukaan_bola_segmental}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_bola_segmental()