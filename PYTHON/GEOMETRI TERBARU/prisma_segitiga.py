# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Prisma Segitiga

PHI = 3.14

def hitung_prisma_segitiga(alas, tinggi, tinggi_prisma):
    volume = round((1/2) * alas * tinggi * tinggi_prisma)
    luas_permukaan = round((alas + 2 * tinggi + 2 * (alas * tinggi)) + (2 * (1/2) * alas * tinggi))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Prisma Segitiga\033[0m")
print("-------------------------------------------------------------")
while True:
    alas_prisma = float(input("Masukkan alas segitiga: "))
    tinggi_prisma = float(input("Masukkan tinggi segitiga: "))
    tinggi_prisma_segitiga = float(input("Masukkan tinggi prisma: "))
    volume_prisma, luas_permukaan_prisma = hitung_prisma_segitiga(alas_prisma, tinggi_prisma, tinggi_prisma_segitiga)
    print("\nPrisma Segitiga:")
    print(f"Volume:\t\t{volume_prisma}")
    print(f"Luas Permukaan:\t{luas_permukaan_prisma}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_prisma_segitiga()