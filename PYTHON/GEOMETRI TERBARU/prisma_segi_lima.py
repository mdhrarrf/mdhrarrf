# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Prisma Segi Lima

PHI = 3.14

def hitung_prisma_segi_lima(sisi, tinggi_prisma):
    volume = round((5/2) * (sisi ** 2) * (5 ** 0.5) * tinggi_prisma)
    luas_permukaan = round(5 * sisi * tinggi_prisma + (5/2) * (sisi ** 2) * (5 ** 0.5))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Prisma Segi Lima\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi_prisma_lima = float(input("Masukkan panjang sisi prisma segi lima: "))
    tinggi_prisma_segi_lima = float(input("Masukkan tinggi prisma segi lima: "))
    volume_prisma_segi_lima, luas_permukaan_prisma_segi_lima = hitung_prisma_segi_lima(sisi_prisma_lima, tinggi_prisma_segi_lima)
    print("\nPrisma Segi Lima:")
    print(f"Volume:\t\t{volume_prisma_segi_lima}")
    print(f"Luas Permukaan:\t{luas_permukaan_prisma_segi_lima}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_prisma_segi_lima()