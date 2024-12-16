# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Limas Segi Enam

PHI = 3.14

def hitung_limas_segi_enam(sisi, tinggi_limas):
    volume = round((1/3) * (3 * (3 ** 0.5) / 2) * (sisi ** 2) * tinggi_limas)
    luas_permukaan = round((3 * (3 ** 0.5) / 2) * (sisi ** 2) + 6 * (sisi * (tinggi_limas ** 2) ** 0.5))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Limas Segi Enam\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi_limas_enam = float(input("Masukkan panjang sisi limas segi enam: "))
    tinggi_limas_segi_enam = float(input("Masukkan tinggi limas: "))
    volume_limas_segi_enam, luas_permukaan_limas_segi_enam = hitung_limas_segi_enam(sisi_limas_enam, tinggi_limas_segi_enam)
    print("\nLimas Segi Enam:")
    print(f"Volume:\t\t{volume_limas_segi_enam}")
    print(f"Luas Permukaan:\t{luas_permukaan_limas_segi_enam}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_limas_segi_enam()