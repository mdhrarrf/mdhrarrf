# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Tabung Silinder

PHI = 3.14

def hitung_tabung_silinder(jari_jari, tinggi):
    volume = round(PHI * (jari_jari ** 2) * tinggi)
    luas_permukaan = round(2 * PHI * jari_jari * (jari_jari + tinggi))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Tabung Silinder\033[0m")
print("-------------------------------------------------------------")
while True:
    jari_jari_tabung_silinder = float(input("Masukkan jari-jari tabung silinder: "))
    tinggi_tabung_silinder = float(input("Masukkan tinggi tabung silinder: "))
    volume_tabung_silinder, luas_permukaan_tabung_silinder = hitung_tabung_silinder(jari_jari_tabung_silinder, tinggi_tabung_silinder)
    print("\nTabung Silinder:")
    print(f"Volume:\t\t{volume_tabung_silinder}")
    print(f"Luas Permukaan:\t{luas_permukaan_tabung_silinder}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_tabung_silinder()