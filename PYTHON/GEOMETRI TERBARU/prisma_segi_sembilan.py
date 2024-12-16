# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Prisma Segi Sembilan

PHI = 3.14

def hitung_prisma_segi_sembilan(sisi, tinggi_prisma):
    volume = round((9/4) * (sisi ** 2) * (9 ** 0.5) * tinggi_prisma)
    luas_permukaan = round(9 * sisi * tinggi_prisma + (9/4) * (sisi ** 2) * (9 ** 0.5))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Prisma Segi Sembilan\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi_prisma_sembilan = float(input("Masukkan panjang sisi prisma segi sembilan: "))
    tinggi_prisma_segi_sembilan = float(input("Masukkan tinggi prisma segi sembilan: "))
    volume_prisma_segi_sembilan, luas_permukaan_prisma_segi_sembilan = hitung_prisma_segi_sembilan(sisi_prisma_sembilan, tinggi_prisma_segi_sembilan)
    print("\nPrisma Segi Sembilan:")
    print(f"Volume:\t\t{volume_prisma_segi_sembilan}")
    print(f"Luas Permukaan:\t{luas_permukaan_prisma_segi_sembilan}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_prisma_segi_sembilan()