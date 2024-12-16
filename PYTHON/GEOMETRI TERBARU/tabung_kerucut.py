# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Tabung Kerucut

PHI = 3.14

def hitung_tabung_kerucut(jari_jari, tinggi):
    volume = round(PHI * (jari_jari ** 2) * tinggi)
    luas_permukaan = round(PHI * jari_jari * (jari_jari + (tinggi ** 2 + jari_jari ** 2) ** 0.5))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Tabung Kerucut\033[0m")
print("-------------------------------------------------------------")
while True:
    jari_jari_tabung_kerucut = float(input("Masukkan jari-jari tabung kerucut: "))
    tinggi_tabung_kerucut = float(input("Masukkan tinggi tabung kerucut: "))
    volume_tabung_kerucut, luas_permukaan_tabung_kerucut = hitung_tabung_kerucut(jari_jari_tabung_kerucut, tinggi_tabung_kerucut)
    print("\nTabung Kerucut:")
    print(f"Volume:\t\t{volume_tabung_kerucut}")
    print(f"Luas Permukaan:\t{luas_permukaan_tabung_kerucut}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_tabung_kerucut()