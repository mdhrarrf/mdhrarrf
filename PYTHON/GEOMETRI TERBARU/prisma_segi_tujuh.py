# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Prisma Segi Tujuh

PHI = 3.14

def hitung_prisma_segi_tujuh(sisi, tinggi_prisma):
    volume = round((7/4) * (sisi ** 2) * (7 ** 0.5) * tinggi_prisma)
    luas_permukaan = round(7 * sisi * tinggi_prisma + (7/4) * (sisi ** 2) * (7 ** 0.5))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Prisma Segi Tujuh\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi_prisma_tujuh = float(input("Masukkan panjang sisi prisma segi tujuh: "))
    tinggi_prisma_segi_tujuh = float(input("Masukkan tinggi prisma segi tujuh: "))
    volume_prisma_segi_tujuh, luas_permukaan_prisma_segi_tujuh = hitung_prisma_segi_tujuh(sisi_prisma_tujuh, tinggi_prisma_segi_tujuh)
    print("\nPrisma Segi Tujuh:")
    print(f"Volume:\t\t{volume_prisma_segi_tujuh}")
    print(f"Luas Permukaan:\t{luas_permukaan_prisma_segi_tujuh}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_prisma_segi_tujuh()