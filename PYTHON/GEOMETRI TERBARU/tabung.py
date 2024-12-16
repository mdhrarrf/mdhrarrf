# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Tabung

PHI = 3.14

def hitung_tabung(jari_jari, tinggi):
    volume = round(PHI * (jari_jari ** 2) * tinggi)
    luas_permukaan = round(2 * PHI * jari_jari * (jari_jari + tinggi))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Tabung\033[0m")
print("-------------------------------------------------------------")
while True:
    jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))
    tinggi_tabung = float(input("Masukkan tinggi tabung: "))
    volume_tabung, luas_permukaan_tabung = hitung_tabung(jari_jari_tabung, tinggi_tabung)
    print("\nTabung:")
    print(f"Volume:\t\t{volume_tabung}")
    print(f"Luas Permukaan:\t{luas_permukaan_tabung}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_tabung()