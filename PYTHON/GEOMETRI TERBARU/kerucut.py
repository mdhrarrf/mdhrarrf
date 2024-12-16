# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Kerucut

PHI = 3.14

def hitung_kerucut(jari_jari, tinggi):
    volume = round((1/3) * PHI * (jari_jari ** 2) * tinggi)
    luas_permukaan = round(PHI * jari_jari * (jari_jari + tinggi))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Kerucut\033[0m")
print("-------------------------------------------------------------")
while True:
    jari_jari_kerucut = float(input("Masukkan jari-jari kerucut: "))
    tinggi_kerucut = float(input("Masukkan tinggi kerucut: "))
    volume_kerucut, luas_permukaan_kerucut = hitung_kerucut(jari_jari_kerucut, tinggi_kerucut)
    print("\nKerucut:")
    print(f"Volume:\t\t{volume_kerucut}")
    print(f"Luas Permukaan:\t{luas_permukaan_kerucut}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_kerucut()