# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Prisma Segiempat

PHI = 3.14

def hitung_prisma_segiempat(panjang, lebar, tinggi_prisma):
    volume = round(panjang * lebar * tinggi_prisma)
    luas_permukaan = round(2 * (panjang * lebar + panjang * tinggi_prisma + lebar * tinggi_prisma))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Prisma Segiempat\033[0m")
print("-------------------------------------------------------------")
while True:
    panjang_prisma = float(input("Masukkan panjang prisma: "))
    lebar_prisma = float(input("Masukkan lebar prisma: "))
    tinggi_prisma_segiempat = float(input("Masukkan tinggi prisma: "))
    volume_prisma_segiempat, luas_permukaan_prisma_segiempat = hitung_prisma_segiempat(panjang_prisma, lebar_prisma, tinggi_prisma_segiempat)
    print("\nPrisma Segiempat:")
    print(f"Volume:\t\t{volume_prisma_segiempat}")
    print(f"Luas Permukaan:\t{luas_permukaan_prisma_segiempat}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_prisma_segiempat()