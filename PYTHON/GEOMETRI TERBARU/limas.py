# Muhammad Haidar Almer Rafif
# 16/12/24
# Program Menghitung Limas

PHI = 3.14

def hitung_limas(panjang, lebar, tinggi):
    volume = round((1/3) * panjang * lebar * tinggi)
    luas_permukaan = round(panjang * lebar + 2 * (panjang * tinggi + lebar * tinggi))
    return volume, luas_permukaan

print("\033[1;34mProgram Geometri: Menghitung Volume dan Luas Permukaan Limas\033[0m")
print("-------------------------------------------------------------")
while True:
    panjang_limas = float(input("Masukkan panjang limas: "))
    lebar_limas = float(input("Masukkan lebar limas: "))
    tinggi_limas = float(input("Masukkan tinggi limas: "))
    volume_limas, luas_permukaan_limas = hitung_limas(panjang_limas, lebar_limas, tinggi_limas)
    print("\nLimas:")
    print(f"Volume:\t\t{volume_limas}")
    print(f"Luas Permukaan:\t{luas_permukaan_limas}")
    print()
    if input("Hitung lagi? (y/n): ").lower() != 'y':
        break
hitung_limas()