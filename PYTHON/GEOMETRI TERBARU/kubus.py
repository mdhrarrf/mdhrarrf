# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Kubus

PHI = 3.14

def hitung_kubus(sisi):
    volume = round(sisi ** 3)
    luas_permukaan = round(6 * (sisi ** 2))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Kubus\033[0m")
print("-------------------------------------------------------------")
while True:
    sisi_kubus = float(input("Masukkan sisi kubus: "))
    volume_kubus, luas_permukaan_kubus = hitung_kubus(sisi_kubus)
    print("\nKubus:")
    print(f"Volume:\t\t{volume_kubus}")
    print(f"Luas Permukaan:\t{luas_permukaan_kubus}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_kubus()