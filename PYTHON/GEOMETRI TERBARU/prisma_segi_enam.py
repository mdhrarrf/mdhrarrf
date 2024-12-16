# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Prisma Segi Enam

PHI = 3.14

def hitung_prisma_segi_enam(sisi, tinggi_prisma):
    volume = round((3 * (3 ** 0.5) / 2) * (sisi ** 2) * tinggi_prisma)
    luas_permukaan = round(6 * sisi * tinggi_prisma + 3 * (3 ** 0.5) * (sisi ** 2))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Prisma Segi Enam\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi_prisma = float(input("Masukkan panjang sisi prisma segi enam: "))
    tinggi_prisma_segi_enam = float(input("Masukkan tinggi prisma segi enam: "))
    volume_prisma_segi_enam, luas_permukaan_prisma_segi_enam = hitung_prisma_segi_enam(sisi_prisma, tinggi_prisma_segi_enam)
    print("\nPrisma Segi Enam:")
    print(f"Volume:\t\t{volume_prisma_segi_enam}")
    print(f"Luas Permukaan:\t{luas_permukaan_prisma_segi_enam}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_prisma_segi_enam()