# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Bola

PHI = 3.14

def hitung_bola(jari_jari):
    volume = round((4/3) * PHI * (jari_jari ** 3))
    luas_permukaan = round(4 * PHI * (jari_jari ** 2))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Bola\033[0m")
print("-------------------------------------------------------------")
while True:
    jari_jari_bola = float(input("Masukkan jari-jari bola: "))
    volume_bola, luas_permukaan_bola = hitung_bola(jari_jari_bola)
    print("\nBola:")
    print(f"Volume:\t\t{volume_bola}")
    print(f"Luas Permukaan:\t{luas_permukaan_bola}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_bola()