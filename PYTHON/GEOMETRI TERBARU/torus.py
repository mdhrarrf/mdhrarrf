# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Torus

PHI = 3.14

def hitung_torus(jari_jari_dalam, jari_jari_luar):
    volume = round(2 * PHI * (jari_jari_dalam ** 2) * (PHI * jari_jari_luar))
    luas_permukaan = round(2 * PHI * jari_jari_luar * (2 * PHI * jari_jari_dalam))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Torus\033[0m")
print("-------------------------------------------------------------")
while True:
    jari_jari_dalam_torus = float(input("Masukkan jari-jari dalam torus: "))
    jari_jari_luar_torus = float(input("Masukkan jari-jari luar torus: "))
    volume_torus, luas_permukaan_torus = hitung_torus(jari_jari_dalam_torus, jari_jari_luar_torus)
    print("\nTorus:")
    print(f"Volume:\t\t{volume_torus}")
    print(f"Luas Permukaan:\t{luas_permukaan_torus}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_torus()