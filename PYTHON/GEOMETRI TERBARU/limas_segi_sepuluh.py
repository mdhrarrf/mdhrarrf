# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Limas Segi Sepuluh

PHI = 3.14

def hitung_limas_segi_sepuluh(sisi, tinggi_limas):
    volume = round((1/3) * (5 * (5 + 2 * (5 ** 0.5)) * (sisi ** 2) * tinggi_limas) / 2)
    luas_permukaan = round(5 * sisi * (tinggi_limas ** 2) ** 0.5 + (5/2) * (sisi ** 2) * (5 ** 0.5))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Limas Segi Sepuluh\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi_limas_sepuluh = float(input("Masukkan panjang sisi limas segi sepuluh: "))
    tinggi_limas_segi_sepuluh = float(input("Masukkan tinggi limas: "))
    volume_limas_segi_sepuluh, luas_permukaan_limas_segi_sepuluh = hitung_limas_segi_sepuluh(sisi_limas_sepuluh, tinggi_limas_segi_sepuluh)
    print("\nLimas Segi Sepuluh:")
    print(f"Volume:\t\t{volume_limas_segi_sepuluh}")
    print(f"Luas Permukaan:\t{luas_permukaan_limas_segi_sepuluh}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_limas_segi_sepuluh()