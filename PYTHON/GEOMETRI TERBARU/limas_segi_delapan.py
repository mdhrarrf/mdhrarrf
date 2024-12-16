# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Limas Segi Delapan

PHI = 3.14

def hitung_limas_segi_delapan(sisi, tinggi_limas):
    volume = round((1/3) * 2 * (1 + (2 ** 0.5)) * (sisi ** 2) * tinggi_limas)
    luas_permukaan = round(2 * (1 + (2 ** 0.5)) * (sisi ** 2) + 4 * sisi * (tinggi_limas ** 2) ** 0.5)
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Limas Segi Delapan\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi_limas = float(input("Masukkan panjang sisi limas segi delapan: "))
    tinggi_limas_segi_delapan = float(input("Masukkan tinggi limas: "))
    volume_limas_segi_delapan, luas_permukaan_limas_segi_delapan = hitung_limas_segi_delapan(sisi_limas, tinggi_limas_segi_delapan)
    print("\nLimas Segi Delapan:")
    print(f"Volume:\t\t{volume_limas_segi_delapan}")
    print(f"Luas Permukaan:\t{luas_permukaan_limas_segi_delapan}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_limas_segi_delapan()